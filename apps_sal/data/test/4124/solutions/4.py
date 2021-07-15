def mi():
	return map(int, input().split())

a = list(input())[::-1]
b = list(input())[::-1]

s = -1
for i in range(min(len(a),len(b))):
	if a[i]!=b[i]:
		s = i
		break
if s==-1:
	print (abs(len(a)-len(b)))
else:
	print (len(a)+len(b)-2*s)
