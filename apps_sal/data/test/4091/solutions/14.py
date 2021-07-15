n, k = list(map(int, input().split()))

a = list(map(int, input().split()))

at = []

z = 0
for i in a:
    at.append( (z, i) )
    z = z + 1

at.sort(key = lambda x:-x[1])

zt = sorted(at[:k], key = lambda x:x[0])

prev = -1
ai = []
suma = 0
for i in zt:
    ai.append(i[0] - prev)
    prev = i[0]
    suma += i[1]


ai[-1] = ai[-1] + (n - sum(ai))

print(suma)
print(" ".join(str(i) for i in ai))

