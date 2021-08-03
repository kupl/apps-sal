N, K = (int(x) for x in input().split())

p = list(map(int, input().split()))

ans = 0
p.sort()

for i in range(0, K):
    ans += p[i]

print(ans)
