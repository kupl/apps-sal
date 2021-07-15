'''
import sys
sys.stdin = open("input.txt", "r")
sys.stdout = open("output.txt", "w")
'''
def Solve(a, b, c, l):
	delta = a - b - c
	if delta < 0:
		return 0
	k = min(l, delta) + 1
	return k * (k + 1) // 2

a, b, c, l = list(map(int, input().split()))

ans = (l + 3) * (l + 2) * (l + 1) // 6

for d in range(l + 1):
	ans -= Solve(a + d, b, c, l - d) + Solve(b + d, a, c, l - d) + Solve(c + d, a, b, l - d)
print(ans)

