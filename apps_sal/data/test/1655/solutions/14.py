n = int(input())
data = list(map(int, input().split()))
data.reverse()
r = data[0]
ans = 1
for i in range(1, n):
    if i > r:
        ans += 1
    r = max(r, data[i] + i)
print(ans)
