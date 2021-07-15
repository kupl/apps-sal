n, m = map(int, input().split())

s1 = []
s2 = []
for i in range(n):
	s1.append(input())
for i in range(m):
	s2.append(input())

s1 = set(s1)
s2 = set(s2)

g = len(s1.intersection(s2))
w1 = len(s1.difference(s2))
w2 = len(s2.difference(s1))

if w1 > w2:
	print("YES")
elif w1 == w2 and g % 2 != 0:
	print("YES")
else:
	print("NO")
