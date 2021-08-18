n, k = map(int, input().split())
data = list(map(int, input().split()))
l = sorted(data, reverse=True)
ans = 0

for i in range(k):
    ans += l[i]

print(ans)
