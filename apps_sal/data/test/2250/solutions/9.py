for _ in range(int(input())):
    n = int(input())
    s = input()
    if len(set(s)) == 1:
        print((n + 2) // 3)
        continue
    cur = 1
    arr = []
    for i in range(n):
        if s[i] == s[(i + 1) % n]:
            cur += 1
        else:
            arr.append(cur)
            cur = 1
    if s[-1] == s[0]:
        arr[0] += cur - 1
    res = 0
    for e in arr:
        res += e // 3
    print(res)
