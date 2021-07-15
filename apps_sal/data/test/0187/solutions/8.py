n=int(input())
l=[]
for i in range(n):
    l+=[int(input())]
l.sort(key=int)
if l.count(l[0])==n>>1 and l.count(l[-1])==n>>1:
    print("YES")
    print(l[0],l[-1])
else:
    print("NO")

