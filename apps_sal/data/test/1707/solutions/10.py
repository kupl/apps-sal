n = int(input())
a = list(map(int, input().split()))
a = sorted(map(abs, a))
ans = 0
j = 1
for i in range(n):
    while j < n and a[j] - a[i] <= a[i]:
        j += 1
    ans += j - i - 1
print(ans)
