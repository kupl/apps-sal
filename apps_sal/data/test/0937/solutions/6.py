
n, m = list(map(int,input().split()))
a = list(map(int,input().split()))
b = list(map(int,input().split()))

s = [0]*n
if b[0]==0:
	s[0] = a[0]
su = 0
for i in range(n):
	if b[i]==1:
		su+=a[i]
for i in range(1,n):
	if b[i]==0:
		s[i] = a[i]
max_init_sum = init_sum = sum(s[:m])
k = m
for i in range(k, n):
	init_sum = init_sum - s[i-k] + s[i]
	#print (init_sum, s[i-k], s[k])
	max_init_sum = max(max_init_sum, init_sum)
print(max_init_sum+su)

