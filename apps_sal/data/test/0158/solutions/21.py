# A. Chess Tourney

n = int(input())
r = list(map(int, input().split()))

r = sorted(r)

f, s = min(r[n:]), max(r[:n])

if f > s:
	print('YES')
else:
	print('NO')

