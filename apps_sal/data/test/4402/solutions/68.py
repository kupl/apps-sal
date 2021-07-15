a,b = map(int, input().split())


if a<=5:
    fee = 0
elif a>=13:
    fee = b
else:
    fee = b//2

print(fee)
