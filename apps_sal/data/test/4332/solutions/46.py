nlist = list(map(int,input()))
rev_n = list(reversed(nlist))
sn = sum(nlist)
n = 0

for i in range(len(nlist)):
    n += rev_n[i]*(10**i) 
if n%sn == 0:
    print("Yes")
else:
    print("No")
