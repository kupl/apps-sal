a, b = map(int, input().split())
total = 0
for i in range(a, b + 1):
    x = str(i)
    y = int(x[::-1])
    if i == y:
        total += 1
print(total)
