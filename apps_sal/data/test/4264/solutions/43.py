n = int(input())
l = list()
for i in range(1, n+1):
    m = list(str(i))
    if len(m) % 2 != 0:
        l.append(i)
print((len(l)))

