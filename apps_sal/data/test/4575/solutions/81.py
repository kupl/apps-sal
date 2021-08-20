N = int(input())
(D, X) = list(map(int, input().split()))
ans = 0
for i in range(1, N + 1):
    a = int(input())
    c = []
    for d in range(D):
        if d * a + 1 > D:
            break
        c.append(d * a + 1)
    ans += len(c)
print(ans + X)
