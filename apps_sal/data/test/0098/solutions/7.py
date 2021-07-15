a, b = (int(x) for x in input().split())
a1, b1 = (int(x) for x in input().split())
a2, b2 = (int(x) for x in input().split())

if ((max(a1,a2) <= a and b1+b2 <= b) or (max(a1,a2) <= b and b1+b2 <= a) or 
	(max(b1,b2) <= a and a1+a2 <= b) or (max(b1,b2) <= b and a1+a2 <= a) or 
	(max(b1,a2) <= a and b2+a1 <= b) or (max(b1,a2) <= b and b2+a1 <= a) or 
	(max(b2,a1) <= a and b1+a2 <= b) or (max(b2,a1) <= b and b1+a2 <= a)):
	print("YES")
else:
	print("NO")
