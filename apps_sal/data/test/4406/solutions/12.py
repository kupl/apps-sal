n,k = map(int,input().split())
l = []
for i in map(int,input().split()):
    if i not in l:
        if len(l)==k:
            del l[-1]
        l.insert(0,i)
print(len(l))
print(*l)
