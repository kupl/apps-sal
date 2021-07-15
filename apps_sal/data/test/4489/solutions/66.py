N = int(input())
ss = [input() for i in range(N)]
M = int(input())
ts = [input() for i in range(M)]

ssset = set(ss)
cnt = 0
for x in ssset:
	cnt = max(cnt, ss.count(x) - ts.count(x))
print(cnt)

