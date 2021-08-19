(n, m) = list(map(int, input().split()))
li = [0] * 1002
for i in range(0, n):
    a = input()
    pG = 0
    pS = 0
    for j in range(0, m):
        if a[j] == 'G':
            pG = j
        elif a[j] == 'S':
            pS = j
    if pS < pG:
        print(-1)
        break
    li[pS - pG] = 1
else:
    ans = 0
    for i in range(1, 1002):
        ans += li[i]
    print(ans)
