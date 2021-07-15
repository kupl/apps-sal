N = int(input())
M = [0] * 100
for i in range(1, N+1):
    i = str(i)
    l, r = int(i[0]), int(i[-1])
    M[l*10+r] += 1
ans = 0
for i, cnt in enumerate(M):
    l, r = divmod(i, 10)
    ans += cnt * M[r*10+l]
print(ans)

