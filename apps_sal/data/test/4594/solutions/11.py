i = input()

l = []

for n in range(int(i)):
    n = input()
    l.append(n)

l = list(set(l))

print((len(l)))
