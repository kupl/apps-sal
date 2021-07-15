n,m=map(int,input().split())
l1 = [0]*n
l2 = [0]*n
for i in range(m):
        p,s=map(str,input().split())
        p= int(p)
        if s == 'AC':
                l2[p-1] +=1
        else:
                if l2[p-1] == 0:
                        l1[p-1] +=1
cntac = 0
cntwa = 0
for i in range(n):
        if l2[i] != 0:
                cntac +=1
                cntwa += l1[i]

                
                
print(cntac,cntwa)
