x = int(input())
res = 0
for b in range(x + 1):
    for p in range(2, x + 2):
        if res < b ** p <= x:
            res = b ** p
        elif b ** p > x:
            break
print(res)
