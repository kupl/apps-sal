n = int(input())
a = [int(i) for i in input().split()]
cost = []
for i in range(-100, 101):
    tmp = 0
    for j in a:
        tmp += (j - i) ** 2
    cost.append(tmp)
print(min(cost))
