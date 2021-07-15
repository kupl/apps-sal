n = int(input())
a = [int(x) for x in input().split()]
a.sort()
if a[1]-a[0]>a[-1]-a[-2]:
	del a[0]
else:
	del a[-1]
print(a[-1]-a[0])
