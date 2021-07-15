n = int(input())
k = list(map(int,input().split()))
m = [0]*n
for i in range(n):
	t = list(map(int,input().split()))
	for j in range(k[i]):
		m[i] += t[j] * 5 + 15
print(min(m))
		

