n, w = list(map(int, input().split()))
a = list(map(int, input().split()))
prefix = [0]
summ = 0
for i in range(n):
	summ += a[i]
	prefix.append(summ)
r = max(prefix)
t = min(prefix)
cnt1 = 0
if t < 0:
	cnt1 += abs(t)
cnt2 = w - r
if cnt2 - cnt1 + 1 <= 0:
	print(0)
else:	
	print(cnt2 - cnt1 + 1)	


