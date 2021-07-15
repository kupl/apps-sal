n = int(input())

money_sum = 0

for i in range(n):
    x,u = input().split()
    x = float(x)
    if u == "JPY":
        money_sum += x
    else:
        money_sum += x*380000
print(money_sum)
