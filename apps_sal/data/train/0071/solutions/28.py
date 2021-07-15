gans = []
for _ in range(int(input())):
    n = int(input())
    u = list(map(int, input().split()))
    cur = 0
    ans = 0
    for i in range(n):
        if u[i] == 0:
            continue
        if u[i] > 0:
            cur += u[i]
        else:
            u[i] = -u[i]
            if cur > u[i]:
                cur -= u[i]
            else:
                ans += u[i] - cur
                cur = 0
        #print(cur, u[i])
    gans.append(ans)
print('\n'.join(map(str, gans)))

