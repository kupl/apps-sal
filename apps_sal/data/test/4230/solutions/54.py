x, n = map(int, input().split())

p = list(map(int, input().split()))

l = list()

k = list()

for i in range(102):
    if i not in p:
        l.append(i)

for i in range(len(l)):
    k.append(abs(x - l[i]))

m = k.index(min(k))

print(l[m])
