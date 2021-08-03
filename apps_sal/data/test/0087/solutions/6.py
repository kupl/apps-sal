m, d = list(map(int, input().split()))
a31 = [1, 3, 5, 7, 8, 10, 12]
c = 30
if m in a31:
    c = 31
elif m == 2:
    c = 28
c -= (8 - d)
print(1 + (c + 6) // 7)
