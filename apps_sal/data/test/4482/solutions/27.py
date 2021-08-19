def cost(x):
    cost = (x - ave) ** 2
    return cost


n = input()
a = list(map(int, input().split()))
ave = round(sum(a) / int(n))
print(sum(list(map(cost, a))))
