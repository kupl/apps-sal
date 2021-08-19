# B - Toll Gates
# https://atcoder.jp/contests/abc094/tasks/abc094_b

n, m, x = list(map(int, input().split()))
a = list(map(int, input().split()))

cost1 = 0
cost2 = 0

for i in range(x, 0, -1):
    if i in a:
        cost1 += 1

for i in range(x, n):
    if i in a:
        cost2 += 1

cost = [cost1, cost2]
print((min(cost)))
