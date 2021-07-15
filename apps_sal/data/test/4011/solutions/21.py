n = int(input())
s = input()
perm = list(map(int,input().split()))
wyn = list(map(int,s))
c = 0
for i in range(n):
	if c == 1:
		break
	if perm[int(s[i])-1] > int(s[i]):
		wyn[i] = perm[int(s[i])-1]
		j = i 
		c = 1
		while True:
			j += 1
			if j < n and perm[int(s[j])-1] >= int(s[j]):
					wyn[j] = perm[int(s[j])-1]
			else:
				break
for i in wyn:
	print(i, end = "")
