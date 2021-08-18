
num = int(input())
total = 0
for i in range(num):
    money, code = input().split()
    if code == "JPY":
        total += float(money)
    elif code == "BTC":
        total += float(money) * 380000.0
print(total)
