n, l = map(int, input().split())

l1 = [int(x) for x in input().split()]
l2 = [int(x) for x in input().split()]

s1 = ''

prev = -1
for i in range(n):
	s1 += '0' * (l1[i] - prev - 1) + '1'
	prev = l1[i]
s1 += '0' * (l - prev - 1)

s2 = ''

prev = -1
for i in range(n):
	s2 += '0' * (l2[i] - prev - 1) + '1'
	prev = l2[i]
s2 += '0' * (l - prev - 1)

s1 = s1 * 2

if s1.find(s2) != -1:
	print("YES")
else:
	print("NO")
