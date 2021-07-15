def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

def isCoprime(a,b):
	if gcd(a,b) == 1:
		return True
	else:
		return False

def main():
	(l,r) = map(int, input().split())
	for a in range(l,r-1):
		for b in range(a+1,r):
			if isCoprime(a,b)==True:
				for c in range(b+1,r+1):
					if isCoprime(b,c)==True:
						if isCoprime(a,c) == False:
							print(a,b,c)
							return
	print(-1)
	return

def __starting_point():
	main()
__starting_point()
