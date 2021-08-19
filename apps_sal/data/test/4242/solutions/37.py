(a, b, k) = map(int, input().split())
c = []
for i in range(1, 101):
    if a % i == 0:
        if b % i == 0:
            c.append(i)
print(c[-k])
