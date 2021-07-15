n = int(input())
m = int(input())
a = list(map(int, input().rstrip().split()))
b = list(map(int, input().rstrip().split()))
fuel_used = 0
for i in range(n-1):
	fuel_used += (1-fuel_used)/a[i]
	fuel_used += (1-fuel_used)/b[i+1]
fuel_used += (1-fuel_used)/a[n-1]
fuel_used += (1-fuel_used)/b[0]
try:
	fuel_required = m*(fuel_used)/(1-fuel_used)
	print(fuel_required)
except ZeroDivisionError:
	print(-1)
