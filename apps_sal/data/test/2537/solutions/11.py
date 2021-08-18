from collections import Counter
for _ in range(int(input())):
    s = input()
    t = input()
    p = input()
    cp = dict(Counter(p))
    i = 0
    j = 0
    lt = len(t)
    arr = [0] * lt
    ls = len(s)
    while i < ls and j < lt:
        if s[i] == t[j]:
            arr[j] = t[j]
            i += 1
            j += 1
        else:
            j += 1
    if i != ls:
        print("NO")
    else:
        flag = 0
        for i in range(lt):
            if arr[i] == 0:
                try:
                    cp[t[i]] -= 1
                    if cp[t[i]] < 0:
                        flag = 1
                        break
                    arr[i] = t[i]
                except:
                    flag = 1
                    break
        print("YES" if flag == 0 else "NO")
