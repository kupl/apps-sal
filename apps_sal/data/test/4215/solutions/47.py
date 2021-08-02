a, b = list(map(int, input().split()))

if a <= b or a - (b * 2) <= 0:
    print("0")

else:
    print((a - (b * 2)))
