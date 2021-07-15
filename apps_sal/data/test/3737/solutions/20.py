n = int(input())
k = list(map(int, input().split()))
mn = min(k)
mx = max(k)
ans = 0
for i in k:
    if (mn != i != mx):
        ans += 1
print(ans)
