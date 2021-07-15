import sys
f=sys.stdin
out=sys.stdout

n,k=map(int,f.readline().rstrip('\r\n').split())
if k%n==0:
	out.write(str(k//n)+'\n')
else:
	out.write(str((k//n)+1)+'\n')
