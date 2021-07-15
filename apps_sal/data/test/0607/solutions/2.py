n, p = list(map(int,input().split()))
sil = [1] * 300000
sil[0] = 1
sil[1] = 1
for i in range(2,300000):
	sil[i] = (sil[i-1]*i)%p
wyn = 0
for i in range(n):
	wyn = (wyn + (n-i)*sil[n-i]*sil[i+1])%p
print(wyn)

