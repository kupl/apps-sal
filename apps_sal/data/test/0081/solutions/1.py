a, b = list(map(int,input().split()))
def gcd(x,y):
	if x == 0:
		return y
	if y == 0:
		return x
	if y > x:
		y,x = x,y
	return gcd(x%y, y)
if a > b:
	a, b = b, a
k = b - a
dzielniki = []
i = 1
while i ** 2 <= k:
	if k % i == 0:
		dzielniki.append(i)
		dzielniki.append(k // i)
	i+= 1
gcdd = a * b / gcd(a,b)
wynik = 0
#print(dzielniki)
for d in dzielniki:
	aa = a - (a % d) + d
	bb = b - (b % d) + d
	#print(aa,bb)
	if aa * bb // gcd(aa,bb) <= gcdd:
		if aa * bb // gcd(aa,bb) == gcdd:
			wynik = min(d-(a%d),wynik)
		else:
			gcdd = aa * bb // gcd(aa,bb)
			wynik = d-(a%d)
print(wynik)

