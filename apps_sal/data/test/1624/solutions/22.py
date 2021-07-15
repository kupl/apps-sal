n = int(input())
a = [int(j) for j in input().split()]
a.sort()
su = 0
for x in range(int(len(a)/2)):
	# print(a[x], a[n-x-1])
	su += (a[x] + a[n-x-1])**2
print(su)
