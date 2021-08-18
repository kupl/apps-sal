def nono(nu, a, b, c):
    if c == len(nu):
        return a
    if nu[c] >= b:
        silo = b * (2**(c + 1) - 1)
        return nono(nu, max(a, silo), b // 2, c + 1)
    else:
        silo = nu[c] * (2**(c + 1) - 1)
        return nono(nu, max(a, silo), nu[c] // 2, c + 1)


n = int(input())
nums = list(map(int, input().split()))
mapa = {}
li = []
for nu in nums:
    mapa[nu] = mapa.get(nu, 0) + 1
for ma, c in list(mapa.items()):
    li.append(c)
li.sort(reverse=True)
res = li[0]
nu = li
a = li[0]
b = li[0] // 2
c = 1
while len(nu) > c:
    if nu[c] >= b:
        silo = b * (2**(c + 1) - 1)
        a = max(a, silo)
        b = b // 2
        c += 1
    else:
        silo = nu[c] * (2**(c + 1) - 1)
        a = max(a, silo)
        b = nu[c] // 2
        c += 1
print(a)
