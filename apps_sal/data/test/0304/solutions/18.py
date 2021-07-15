n = input()
all = [0] * 10
for x in n:
	all[int(x)]+=1

dp = [0] * 20
dp[0] = 1
for i in range(1, 10):
	cur = [0] * 20
	if(all[i] > 0):
		for le in range(0, 20):     
			fac = 1
			zn = 1
			for kol in range(1, all[i] + 1):
				if(le + kol < 20):
					zn *= le + kol
					fac *= kol
					cur[le + kol] +=  (zn // fac) * dp[le]
		dp = cur


cur = [0] * 20
if(all[0] > 0):
	for le in range(1, 20):
		fac = 1
		zn = 1
		for kol in range(1, all[0] + 1):
			if(le + kol < 20):
				zn *= (le + kol-1)
				fac *= kol
				cur[le + kol] +=  (zn // fac) * dp[le]
	dp = cur

print(sum(dp))

