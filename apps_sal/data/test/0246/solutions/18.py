def calc(n):
	val = n
	cnt = 0
	while(val):
		cnt += val%10
		val//=10
	return n-cnt
		
n,s = list(map(int,input().split()))
if n<=s:
	print(0)
	return
val = s
val //= 10
if val==0:
	print(n-9 if n>=9 else 0)
	return
val *= 10
while calc(val)<s:
	val += 10
	if val>n:
		print(0)
		break
else:
	print(n-val+1)

