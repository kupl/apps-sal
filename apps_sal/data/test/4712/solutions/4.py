h,w = map(int,input().split())
l=[]
[l.append(input()) for _ in range(h)]

print("#"*(w + 2))
for s in l:
    print("#",s,"#",sep='')

print("#"*(w + 2))
