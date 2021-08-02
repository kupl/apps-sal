x = int(input())
c = 1
for b in range(1, 32):
    for p in range(2, 10):
        if b**p <= x:
            c = max(c, b**p)
        else:
            break
print(c)
