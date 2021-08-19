n = int(input())
a = [int(x) for x in input().split()]
avg = round(sum(a) / n)
cost = 0
for e in a:
    cost += (e - avg) ** 2
print(cost)
