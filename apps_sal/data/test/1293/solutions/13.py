n = int(input())
a = [int(i) for i in input().split()]
a = [0] + a
ans = 0
for i in range(1, n + 1):
    ans += abs(a[i] - a[i - 1])
print(ans)
