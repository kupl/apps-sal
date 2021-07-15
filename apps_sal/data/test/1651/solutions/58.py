s,p = map(int,input().split())
for n in range(1,1000005):
    m = s - n
    if n*m == p:
        print('Yes')
        return
print('No')
