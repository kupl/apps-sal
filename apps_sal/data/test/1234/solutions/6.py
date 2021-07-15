'''input
2 1 2
-1000000000 1000000000

9 2 3
5 2 5 2 4 1 1 3 2
6 1 4
4 1 3 2 2 3
'''
n, m, k = list(map(int, input().split()))
a = list(map(int, input().split()))
b = sorted([(a[i], i) for i in range(n)])
ok = [0] * n
ans = 0
for x, i in b[-k * m:]:
	ok[i] = 1
	ans += x
# print(ok)
t = 0
li = []
for i in range(n):
	t += ok[i]
	if ok[i] and t % m == 0:
		li += [i + 1]
print(ans)
print(*li[:-1])

