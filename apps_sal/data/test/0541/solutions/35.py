x=c=0
for b,a in sorted([[*map(int,t.split())][::-1]for t in open(0)][1:]):
 if a>x:x=b-1;c+=1
print(c)
