a, b, c = list(map(int, input().split()))
L = []
L.append(a)
L.append(b)
L.append(c)

L = list(set(L))

print((len(L)))

