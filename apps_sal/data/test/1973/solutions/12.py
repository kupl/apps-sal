n = int(input())

a = list(map(int,input().split()))
if(n == 1 or n == 2):
    print(n)
    return
notpar = 0
occ = [0 for i in range(10**5 + 1)]
base = 1
gotone = False
leader = -1
leadby = 0
best = 0
occ[a[0]] += 1
cnt = 1
at1 = 1



for i in range(1, n):
    occ[a[i]] +=1
    
    if(occ[a[i]] == 1):
        notpar += 1
        at1 += 1
        cnt += 1
    elif(occ[a[i]] == 2):
        at1 -= 1
    if(occ[a[i]] == base):
        notpar -= 1
    elif(occ[a[i]] > base):
        if(gotone):
            if(a[i] != leader):
                base += 1
                notpar = cnt - 2
                leadby -= 1
                if(leadby == 0):
                    gotone = False
                    leader = -1
            else:
                leadby += 1
        else:
            gotone = True
            leader = a[i]
            leadby = 1
    if(notpar == 0 and (leadby == 1 or (leadby == 0 and base == 1)) or (notpar == 1 and leadby == 0 and at1 > 0)):
        best = i + 1
    if(cnt == 1):
        best = i + 1
    #print(i, base, leader, leadby, gotone, notpar, cnt)
print(best)
                    
                    

