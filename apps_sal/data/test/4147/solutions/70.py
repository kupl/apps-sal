import itertools
N,A,B,C=map(int, input().split())
l=[int(input()) for _ in range(N)]
pattern=["a","b","c","N"]

lcombi=itertools.product(pattern,repeat=N)

ans=(1000)**3
for lc in list(lcombi):
	Alen=0
	Blen=0
	Clen=0
	Acost=0
	Bcost=0
	Ccost=0
	
	if ("a" not in lc) or("b" not in lc) or("c" not in lc):
		continue
	else:
		for i in range(N):
			if lc[i]=="a":
				if Alen==0:Alen+=l[i]
				else:
					Alen+=l[i]
					Acost+=10
			elif lc[i]=="b":
				if Blen==0:Blen+=l[i]
				else:
					Blen+=l[i]
					Bcost+=10
			elif lc[i]=="c":
				if Clen==0:Clen+=l[i]
				else:
					Clen+=l[i]
					Ccost+=10
		Acost+=abs(Alen-A)
		Bcost+=abs(Blen-B)
		Ccost+=abs(Clen-C)
		ans=min(ans,Acost+Bcost+Ccost)

print(ans)
