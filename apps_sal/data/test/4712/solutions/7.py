h,w = map(int, input().split())
a = list(list(input().split()) for _ in range(h))
print("#"*(int(w)+2))
for i in range(h):
    print("#",*a[i],"#",sep="")
print("#"*(int(w)+2))
