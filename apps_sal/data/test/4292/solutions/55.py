N, K = [int(x) for x in input().split()]


p = [int(x) for x in input().split()]
p.sort()

ans = 0
for i in range(K):
    ans += p[i]
print(ans)
