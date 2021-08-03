n, x = list(map(int, input().split()))
bad = 0
for i in range(n):
    a, b = input().split()
    b = int(b)
    if a == '+':
        x += b
    else:
        if x >= b:
            x -= b
        else:
            bad += 1

print(x, bad)
