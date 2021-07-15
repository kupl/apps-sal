n=int(input())
sp=[list(input().split()) for _ in range(n)]
for i in sp:
    i[1]=100-int(i[1])
for i in range(n):
    sp[i].append(i+1)
sp.sort()
for i in sp:
    print((i[2]))

