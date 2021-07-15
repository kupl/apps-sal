N = int(input())
primes=0
for i in range(2,N+1):
	flag=1
	for a in range(2,i//2+1):
		if i%a==0:
			flag=0
			break
	if flag:
		primes+=1

print(primes)
