#codeforces_1056A_live
gi = lambda : list(map(int,input().split()))
for k in range(gi()[0]):
	s,a,b,c = gi()
	print(s//c + ((s//c)//a)*b)
