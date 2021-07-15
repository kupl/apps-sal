n = int(input())
a = list(map(int, input().split()))

max_a = max(a)

ans = 0
for i in range(n):
    if abs(ans - max_a/2) > abs(a[i] - max_a/2):
        ans = a[i]

print(max_a, ans)
