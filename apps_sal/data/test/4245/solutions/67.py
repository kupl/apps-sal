a, b = map(int, input().split())
x = 0
for i in range(b):
    if x >= b:
        break
    else:
        if i == 0:
            x += a
        else:
            x += a - 1
print(i)
