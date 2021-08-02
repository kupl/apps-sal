a, b, x = map(int, input().split())
if a % x == 0:
    min = a // x - 1
else:
    min = a // x
max = b // x
print(max - min)
