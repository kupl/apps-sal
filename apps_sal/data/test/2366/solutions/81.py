import collections
N = int(input())
A = list(map(int, input().split()))

coll = collections.Counter(A)

ans = 0
for n in list(coll.values()):
	ans += n * (n - 1) // 2

for i in A:
	print(ans - coll[i] + 1)
