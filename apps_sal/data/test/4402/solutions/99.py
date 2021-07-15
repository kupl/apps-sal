age, fee = map(int, input().split())

if age >= 13:
    print(fee)
elif 6 <= age <= 12:
    print(fee // 2)
else:
    print(0)
