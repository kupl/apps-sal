(N, T) = map(int, input().split())
lsT = list(map(int, input().split()))
tend = T
ans = T
for i in range(1, N):
    if lsT[i] <= tend:
        ans += lsT[i] + T - tend
        tend = lsT[i] + T
    else:
        ans += T
        tend = lsT[i] + T
print(ans)
