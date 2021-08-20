n = int(input())
i = 1
s = 1
while s <= n:
    i += 1
    s += int((1 + i) / 2 * i)
print(i - 1)
