#import sys
#sys.stdin = open('input.txt', 'r')
#sys.stdout = open('output.txt', 'w')

def norm(a, b, c, d):
	if (b * c >= 0):
		return a * abs(c) <= abs(b) <= d * abs(c)
	return -a * abs(c) >= abs(b) >= -d * abs(c)

x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
a2 = y2 - y1
b2 = x1 - x2
c2 = 0 - a2 * x1 - b2 * y1
n = int(input())
ans = 0
for i in range(n):
	a1, b1, c1 = map(int, input().split())
	if (norm(min(x1, x2), (c2 * b1 - c1 * b2), (a1 * b2 - a2 * b1), max(x1, x2)) and norm(min(y1, y2), (c2 * a1 - c1 * a2), (a2 * b1 - a1 * b2), max(y1, y2))):
		ans += 1
print(ans)
