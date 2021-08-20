(n, x) = list(map(int, input().split()))
r = 0
for _ in range(n):
    (a, b) = input().split()
    if a == '+':
        x += int(b)
    elif int(b) <= x:
        x -= int(b)
    else:
        r += 1
print(x, r)
