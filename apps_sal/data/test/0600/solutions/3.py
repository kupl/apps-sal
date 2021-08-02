a = int(input())
b = int(input())

dist = abs(a - b)
half = dist // 2
if dist % 2 == 0:
    print(half * (half + 1))
else:
    print(half * (half + 1) // 2 + (half + 1) * (half + 2) // 2)
