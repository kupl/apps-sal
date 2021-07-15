n = int(input())
nums = list(map(int, input().split()))
mapa = {}

for nu in nums:
	mapa[nu] = mapa.get(nu, 0) + 1
li = [mapa[x] for x in mapa]

li.sort(reverse=True)

a = li[0]
b = li[0]//2
c = 1
while len(li) > c:
	if b == 0:
		break
	if li[c] >= b:
		silo = b * (2**(c+1) - 1)
		a = max(a, silo)
		b = b//2
		c += 1
	else:
		silo = li[c] * (2**(c+1) - 1)
		a = max(a, silo)
		b = li[c]//2
		c += 1
print(a)



