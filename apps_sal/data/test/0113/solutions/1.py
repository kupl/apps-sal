a, b = map(int, input().split(' '))
aa=a
fives = 0
while a%5==0:
	fives += 1
	a /= 5
twos = 0
while a%2==0:
	twos += 1
	a /= 2
x=1

if fives<b:
	x *= 5**(b-fives)
if twos<b:
	x *= 2**(b-twos)

print(x*aa)
