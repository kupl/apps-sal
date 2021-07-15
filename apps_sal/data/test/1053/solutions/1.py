n = int(input())
res = 0
inc = 1
while n > 1:
	res += inc*(n//2)
	n += 1
	n //= 2
	inc *= 2
print(res)

