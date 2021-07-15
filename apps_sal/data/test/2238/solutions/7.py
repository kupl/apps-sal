#input
n=int(input())

#variables
x=(n-1)//2

#start of program
for i in range(x):
	print('*'*(x-i)+'D'*(2*i+1)+'*'*(x-i))
print('D'*n)
for i in range(x):
	print('*'*(i+1)+'D'*(n-2*(i+1))+'*'*(i+1))
