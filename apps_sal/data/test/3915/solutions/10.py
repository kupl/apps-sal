
crivo = [True] * 2000001
crivo[0] = False
crivo[1] = False
for i in range(2,2001):
	if crivo[i]:
		for j in range(i*i,2000001,i):
			crivo[j] = False

a, b = map(float, input().split())
prime = 0
palindromo = 0
control = False
y = -1
for i in range(1,2000000):
	if crivo[i]:
		prime += 1
	
	if str(int(str(i)[::-1])) == str(i) :
		palindromo += 1
				
	if palindromo * (a / b) >= prime:
		y = i			
if y >= 0:
	print (y) 
else: 
	print ("Palindromic tree is better than splay tree")
