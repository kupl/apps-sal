(a, b) = [int(a) for a in input().split()]
for i in range(1, b + 1):
    if a % 10 != 0:
        a = a - 1
    else:
        a = a // 10
print(a)
