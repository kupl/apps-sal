Q = [int(x) for x in input().split(' ')]
w = Q[0]
l = Q[1]
A = [int(x) for x in input().split(' ')]
B = [0 for i in range(w-1)]
i = 0
j = 0
for i in range(w-1):
	if i<l:
		B[i]=A[i]
	else:
		while j<i:
			if j<i-l:
				j=i-l
			t = min(A[i]-B[i],B[j])
			B[i]+=t
			B[j]-=t
			if B[j]==0:
				j+=1
			else:
				break
	#print(B)
#print(A)
#print(B)
print(sum(B[w-l-1:]))

