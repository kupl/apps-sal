n, a, b = list(map(int, input().strip().split()))

x = 1
while True:
    prva = a // x
    druga = b // x
    if prva + druga < n:
        x -= 1
        break
    x += 1
x = min(x, a, b)
print(x)
