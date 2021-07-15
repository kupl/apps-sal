a = int(input())
str_inp = str(input())

for i in range(1, a+1):
	if a%i == 0:
		str_inp = ''.join(reversed(str_inp[0:i])) + str_inp[i:a]

print(str_inp)

