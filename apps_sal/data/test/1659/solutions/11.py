(n, x) = list(map(int, input().split()))
sad = 0
for i in range(n):
    (a, b) = input().split()
    b = int(b)
    if a == '-':
        if x >= b:
            x -= b
        else:
            sad += 1
    else:
        x += b
print(x, sad)
