n = int(input())
l = []
for i in range(n):
    l.append(1)
    while len(l) > 1 and l[-1] == l[-2]:
        l.pop()
        l[-1] += 1
print(*l)
