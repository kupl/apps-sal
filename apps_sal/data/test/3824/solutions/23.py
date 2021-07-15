def main():
	x1,y1 = map(int,input().split())
	x2,y2 = map(int,input().split())
	res = (abs(x2-x1) + abs(y2 - y1) +2)*2
	if x1==x2:
		res +=2
	if y1 == y2:
		res +=2
	print( res)

main()
