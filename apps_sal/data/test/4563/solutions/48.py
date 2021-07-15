n = int(input())
tvote = 1
avote = 1

for i in range(n):
	t, a = [int(n) for n in input().split()]
	k = (tvote-1)//t + 1
	tnow = t * k
	anow = a * k
	if avote > anow:
		k = (avote-1)//a + 1
		tnow = t * k
		anow = a * k
	tvote = tnow
	avote = anow
	
print(avote+tvote)
