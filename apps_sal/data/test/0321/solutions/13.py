def isPrime(n) : 
    # Corner cases 
    if (n <= 1) : 
        return False
    if (n <= 3) : 
        return True
  
    # This is checked so that we can skip  
    # middle five numbers in below loop 
    if (n % 2 == 0 or n % 3 == 0) : 
        return False
  
    i = 5
    while(i * i <= n) : 
        if (n % i == 0 or n % (i + 2) == 0) : 
            return False
        i = i + 6
  
    return True
t=int(input())
for l in range(t):
	a,b=list(map(int,input().split()))
	if(a-b!=1):
		print("NO")
	else:
		if(isPrime(a+b)):
			print('YES')
		else:
			print('NO')


