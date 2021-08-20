(a, b) = [int(i) for i in input().split()]
a = max(a, 1)
b = max(b, 1)
pr = 1
for i in range(a + 1, b + 1):
    pr = pr * i
    pr = pr % 10
    if pr == 0:
        break
print(pr)
