a1,a2,a3 = map(int, input().split())
b1,b2,b3 = map(int, input().split())
n = int(input())
if((a1+a2+a3+4)//5+(b1+b2+b3+9)//10<=n):
	print('YES')
else:
	print('NO')
