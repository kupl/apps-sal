n = int(input())
s = list(map(int,input().split()))

ans = 0
smax = -10**9
smin = 10**9

for i in s:
	if i > smax:
		smax = i
	if i < smin:
		smin = i

f1 = False
f2 = False

for i in s:
	if (not f1) and (i == smax):
		ans += smax
		f1 = True
		continue

	if (not f2) and (i == smin):
		ans -= smin
		f2 = True
		continue

	if i > 0:
		ans += i
	else:
		ans -= i;

print(ans);
  

