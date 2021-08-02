a, b = list(map(int, input().split()))
s = -1
for i in range(60, 0, -1):
    if a & (1 << i) == 0 and b & (1 << i) != 0:
        print((1 << (i + 1)) - 1)
        break
else:
    print(a ^ b)
