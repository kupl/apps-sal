n = int(input())
a = list(map(int, input().split()))
rates = [0] * 8
cnt = 0

for i in range(n):
    if a[i] < 3200:
        rates[a[i] // 400] += 1
    else:
        cnt += 1

cn = len(rates) - rates.count(0)
if sum(rates) == 0:
    cmin = 1
else:
    cmin = cn

if all([x < 3200 for x in a]):
    cmax = cn
else:
    cmax = cn + cnt

print(cmin, cmax)
