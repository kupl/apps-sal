n, k = list(map(int,input().split()))
st = input()
a = [0] * 28
for i in range(len(st)):
	a[ord(st[i]) - 97] += 1
if max(a) <= k: print('YES')
else: print('NO')

