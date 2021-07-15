n=int(input())
t=[int(i) for i in input().split()]
v=1
j=1
for i in range(1,n):
	if t[i]>=t[i-1]:
		j+=1
	else:
		v=max(v,j)
		j=1
v=max(v,j)
print(v)
