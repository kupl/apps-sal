import math as m

def main():
	n = int(input())
	s = input()
	l = len(s)
	p = int(m.ceil(l/n))
	if l%n!=0 :
		t = '1'
		for i in range(1,n):
			t+='0'
		for i in range(0,p):
			print(t ,end = '')
	else :
		z = s[0:n]
		t=''
		for i in range(0,p):
			t+=z
		if t > s:
			print(t)
			return

		z = str(int(s[0:n])+1)
		if len(z)>n :
			t = '1'
			for i in range(1,n):
				t+='0'
			for i in range(0,p+1):
				print(t ,end = '')
			return

		t=''
		for i in range(0,p):
			t+=z
		
		print(t)
			



main()


	


