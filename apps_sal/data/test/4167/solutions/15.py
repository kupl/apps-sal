(a, b) = list(map(int, input().split()))
if b % 2 == 1:
    print((a // b) ** 3)
else:
    c = (a - b / 2) // b + 1
    print(int((a // b) ** 3 + c ** 3))
