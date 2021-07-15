n = int(input())
a = list(map(int, input().split()))
rates = [0] * 8
cnt = 0

for i in range(n):
  if a[i] < 3200:
    rates[a[i] // 400] += 1
  else:
    cnt += 1
    
cn = len(rates) - rates.count(0) #color number
if sum(rates) == 0:
  cmin = 1
else:
  cmin = cn #color min

if all([x < 3200 for x in a]):
  cmax = cn #color max
else:
  cmax = cn + cnt
  
print(cmin,cmax)
