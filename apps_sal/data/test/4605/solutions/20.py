n, a, b = map(int, input().split())
total = 0
for i in range(1, n + 1):
    x = (str(i))
    j = 0
    total2 = 0
    for j in range(len(x)):
        total2 += int(x[j])
    if a <= total2 <= b:
        total += i
print(total)
