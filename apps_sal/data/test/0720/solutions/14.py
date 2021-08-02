n = int(input())
c = d = counter = 0
for i in range(n):
    a, b = [int(x) for x in input().split()]
    if c != d or i == 0:
        counter += max(min(a, b) - max(c, d) + 1, 0)
    else:
        counter += max(min(a, b) - max(c, d), 0)
    c, d = a, b
print(counter)
