x = int(input())
tmp = 1
for b in range(1, x):
    for p in range(2, x):
        if b ** p <= x:
            tmp = max(tmp, b ** p)
        else:
            break
print(tmp)
