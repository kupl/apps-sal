n = int(input().strip())
money = list(map(int, input().split()))
m = max(money)
pay = 0
for a in money:
    pay += m - a
print(pay)
