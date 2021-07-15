n = int(input())
s = [0]+[int(i) for i in input().split()]
for i in range(n):
	if s[i+1]-s[i]>15:
		print(s[i]+15)
		break
else:
	print(min(s[-1]+15, 90))

