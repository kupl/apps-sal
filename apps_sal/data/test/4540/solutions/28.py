n = int(input())
a = list(map(int, input().split()))
cost = abs(a[0])
for i in range(1, n):
    cost += abs(a[i] - a[i - 1])
cost += abs(a[-1])
ans = [0] * n
an = cost - abs(a[1] - a[0]) - abs(a[0]) + abs(a[1])
print(an)
for i in range(1, n - 1):
    key = cost - abs(a[i - 1] - a[i]) - abs(a[i] - a[i + 1]) + abs(a[i - 1] - a[i + 1])
    print(key)
print(cost - abs(a[-1]) + abs(a[-2]) - abs(a[-1] - a[-2]))
