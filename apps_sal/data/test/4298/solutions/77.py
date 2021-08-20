(n, d) = map(int, input().split())
i = 1
d = 2 * d + 1
while n > d * i:
    i += 1
print(i)
