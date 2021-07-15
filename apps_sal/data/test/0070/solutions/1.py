n, k = map(int, input().split())

A = list(str(n))
A = A[::-1]

_k = k

i = 0
ans = 0

while k and i < len(A):
	if(A[i] != '0'):
		ans += 1
	else:
		k -= 1
	i += 1

if(k):
	if(k != _k):
		print(len(A) - 1)
	else:
		print(len(A))
else:
	print(ans)
