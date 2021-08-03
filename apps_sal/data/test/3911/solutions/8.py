n = int(input())
p = []
while n != 0:
    while len(p) >= 2 and p[-2] == p[-1]:
        p[-2] += 1
        p.pop()
    p.append(1)
    n -= 1
while len(p) >= 2 and p[-2] == p[-1]:
    p[-2] += 1
    p.pop()
print(*p)
