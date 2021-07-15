a,b,x,y = list(map(int,input().rsplit()))
def gdc(a,b):
	if b == 0:
		return a
	return gdc(b,a%b)

g = gdc(x,y)
x //= g
y //= g

print(min(a//x,b//y))
