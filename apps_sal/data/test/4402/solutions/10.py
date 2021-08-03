details = list(map(int, input().split()))
A = details[0]
B = details[1]
if A >= 13:
    print(B)
elif A >= 6 and A <= 12:
    print((int(B / 2)))
else:
    print((0))
