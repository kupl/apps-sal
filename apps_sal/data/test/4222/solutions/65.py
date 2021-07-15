N,*D=open(0);print(int(N.split()[0])-len(set(sum([a.split()for a in D[1::2]],[]))))
