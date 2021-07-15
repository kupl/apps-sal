n = int(input())
list_a = [int(i) for i in input().split()]
ans = 0.0
for i in range(0, n):
    ans += 1 / list_a[i]
    if i == n - 1: ans = 1 / ans
print(ans)
