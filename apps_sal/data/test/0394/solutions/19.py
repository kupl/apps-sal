n = int(input())
a = [0]+[int(i) for i in input().split()]


b = [0] * n 
ans = []

for i in range(1,len(a)):
	b[i-1]=a[i]-a[i-1]


for i in range(1,n):
	if b[:i]==b[-i:]:
		ans.append(n-i)

print(len(ans)+1)
print(*sorted(ans),n)
