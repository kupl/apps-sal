a = int(input())
for i in range((a-1)//2):
	print('*'*((a-2*i-1)//2)+'D'*(2*i+1)+'*'*((a-2*i-1)//2))
print('D'*a)
for i in range((a-1)//2-1,-1,-1):
	print('*'*((a-2*i-1)//2)+'D'*(2*i+1)+'*'*((a-2*i-1)//2))
