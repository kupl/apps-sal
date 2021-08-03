n = int(input())
l = list(map(int, input().split()))
ans = max(l)
for i in range(n):
    ans = min(ans, l[i] // max(i, n - i - 1))
print(ans)
