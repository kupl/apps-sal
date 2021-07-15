k1, k2, k3 = map(int, input().split())
n = k1 + k2 + k3

a = [0] * n
input()
for x in map(int, input().split()):
	a[x-1] = 1
for x in map(int, input().split()):
	a[x-1] = 2


prev = [0, 0, 0]

for i, x in enumerate(a):
	new = [0, 0, 0]

	new[0] = prev[0] + (x!=0)
	new[1] = min(prev[0], prev[1]) + (x!=1)
	new[2] = min(prev) + (x!=2)
	prev = new

print(min(prev))
