n = int(input())
n = bin(n)[2:]
while len(n) < 6:
	n = '0' + n

res = list(n)

res[1], res[5] = res[5] , res[1]
res[2], res[3] = res[3], res[2]


print(int(''.join(res),2))

