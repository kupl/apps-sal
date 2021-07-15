n = int(input())
d = [int(x) for x in input().split(' ')]
s, t = [int(x) for x in input().split(' ')]
a = min(s,t)
b = max(s,t)
x = 0
for i in range(a - 1, b - 1):
	x += d[i]
y = 0
for i in list(range(b - 1, n)) + list(range(a - 1)):
	y += d[i]
print(min(x,y))

