t = int(input())
for u in range(t):
    n = int(input())
    n = n * 4
    x = list(map(int, input().split()))
    x.sort()
    i = 0
    f = []
    while i < n:
        if x[i] == x[i + 1]:
            f += [x[i]]
            i += 2
        else:
            break
    ans = 'YES'
    if len(f) == n // 2:
        ar = f[0] * f[-1]
        i = 0
        j = len(f) - 1
        for k in range(n // 4):
            if f[i] * f[j] != ar:
                ans = 'NO'
                break
            else:
                i += 1
                j -= 1
    else:
        ans = 'NO'
    print(ans)
