n = int(input())
s = list(map(int, input().split()))

ids = []
for i in range(n):
    if s[i] == 1:
        ids.append(i)
#print(ids)

x = len(ids)
c = 1
if len(ids) == 0:
    print(0)
else:
    for i in range(x-1):
        
        diff = ids[i+1] - ids[i]
        #print(diff, 'x')
        #print(c)
        if diff > 2 :
            c += 2
            #print('t')
        else:
            c += diff
        #print(c, i)
        
    print(c)

