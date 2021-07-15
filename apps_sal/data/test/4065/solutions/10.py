import sys
f=sys.stdin
out=sys.stdout

n=int(f.readline().rstrip('\r\n'))
arr=list(map(int,f.readline().rstrip('\r\n').split()))

cnt=1
ma=1

for i in range(1,n):
	if arr[i]<=(2*arr[i-1]):
		cnt+=1
		ma=max(ma,cnt)
	else:
		cnt=1
out.write(str(ma)+"\n")
