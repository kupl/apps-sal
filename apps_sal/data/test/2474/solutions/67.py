n = int(input())
a = list(map(int, input().split()))
a = sorted(a, reverse=True)
cost = 0
for i in range(1, n + 1):
    cost = (cost + a[i - 1] * (i + 1)) % 1000000007
for i in range(1, n):
    cost = cost * 4 % 1000000007
print(cost)
