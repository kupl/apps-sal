(p, n) = map(int, input().split())
x = [int(input()) for i in range(n)]
u = [False] * p
for i in range(min(p + 1, n)):
    if u[x[i] % p]:
        print(i + 1)
        break
    u[x[i] % p] = True
else:
    print(-1)
