n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split())) + [-1]
ans = 0
curr = 0
for i in range(n):
    if (b[curr] >= a[i]):
        ans += 1
        curr += 1
print(ans)
