ar=[]
def generate(n,s):
    if len(s) > 8:return
    if n==0:
        ar.append(int(s))
    for x in range(0,n+1):
        generate(n-x,s+str(x))
    ar.append(int(s+str(n)))
for i in range(1,10):
    generate(10-i,str(i))
ar=sorted(list(set(ar)))
print(ar[int(input())-1])
