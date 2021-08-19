a, b = list(map(int, input().split()))
# a - k = -b + k or b - k
# a + b == 2k or a - b = 0
if a == b:
    print((0))
elif (a + b) % 2 == 0:
    print(((a + b) // 2))
else:
    print("IMPOSSIBLE")
