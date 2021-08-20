(a, b) = list(map(int, input().split()))
num = (b - 1) // 2
if a < b - 1:
    num -= b - 1 - a
print(max(0, num))
