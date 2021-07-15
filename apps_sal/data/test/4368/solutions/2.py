n,k = map(int,input().split())
l = []
while n != 0 :
    r = divmod(n,k)
    n = r[0]
    l.append(r[1])
print(len(l))
