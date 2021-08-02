n = int(input())
k = list()
m = set()
for i in range(n):
    a = input()
    k.append(a)
    m.add(a)
for i in range(n - 1, -1, -1):
    if k[i] in m:
        print(k[i], end='\n')
        m.discard(k[i])
