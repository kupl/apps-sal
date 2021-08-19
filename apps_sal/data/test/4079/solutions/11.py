n = int(input())
for ti in range(n):
    s = input()
    f = [0] * 26
    for i in s:
        f[ord(i) - ord('a')] += 1
    flag = True
    for i in range(26):
        if f[i] > 1:
            flag = False
            break
    if flag:
        s = sorted(s)
        for i in range(len(s) - 1):
            if ord(s[i + 1]) - ord(s[i]) != 1:
                flag = False
                break
        if not flag:
            print('No')
        else:
            print('Yes')
    else:
        print('No')
