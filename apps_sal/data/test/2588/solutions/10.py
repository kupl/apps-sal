import sys
def input():
	return sys.stdin.readline()[:-1]

t = int(input())
ans = []
for _ in range(t):
	n, a, b = map(int, input().split())
	s = input()
	res = [b, 10**30]
	for i in range(n):
		tmp = []
		if s[i] == "0":
			tmp.append(min(res[0]+a+b, res[1]+2*a+b))
			tmp.append(min(res[1]+a+2*b, res[0]+2*a+2*b))
		else:
			tmp.append(10**30)
			tmp.append(res[1]+a+2*b)
		res = tmp
	ans.append(res[0])
print(*ans, sep="\n")
