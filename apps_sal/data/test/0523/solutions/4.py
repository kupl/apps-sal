n, m = list(map(int, input().split()))
s = []
for i in range(n):
	s.append(input())

A, B = '', ''
M = ''
d = {}

for i in range(n):
	for j in range(i+1, n):
		if s[i][::-1] == s[j] and i not in d and j not in d:
			A = A + s[i]
			B = s[j] + B
			
			d[i] = True
			d[j] = True

for i in range(n):
	if s[i][::-1] == s[i] and i not in d:
		M = s[i]

print(len(A) + len(M) + len(B))
print(A + M + B)

