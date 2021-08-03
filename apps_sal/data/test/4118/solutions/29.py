a, b = list(map(int, input().split()))

if 1 <= a * b and a * b <= 81 and a < 10 and b < 10:
    print((a * b))
else:
    print((-1))
