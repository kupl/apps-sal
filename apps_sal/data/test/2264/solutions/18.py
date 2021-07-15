t = int(input())
for i in range(t):
	n = int(input())
	leviy_otr = [10000000000,10000000000]
	pryavi_otr = [-10000000000,-10000000000]
	for j in range(n):
		a = input().split()
		a = [int(a[0]), int(a[1])]
		if leviy_otr[1] > a[1]:
			leviy_otr = a
		if pryavi_otr[0] < a[0]:
			pryavi_otr = a
	print (max(0, pryavi_otr[0] - leviy_otr[1]))
