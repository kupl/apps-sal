F,I,T = input().split();

F = int(F)
I = int(I)
T = int(T)
kitten = 0
acum = 0
v = [0] * I

for i in range(0,F):
	line = input()
	for j in range(0,I):
		if line[j] == 'Y':
			v[j] += 1


for j in range(0,I):
	if v[j] >= T:
		acum += 1

print(acum)

