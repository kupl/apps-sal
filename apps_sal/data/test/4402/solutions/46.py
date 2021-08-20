a = list(map(int, input().split()))
A = a[0]
B = a[1]
if A >= 13:
    print(B)
elif A >= 6 and A <= 12:
    print(int(B / 2))
else:
    print(0)
