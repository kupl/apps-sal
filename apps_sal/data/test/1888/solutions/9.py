n,m = map(int,input().split())
debts = [0]*n
credit = [0]*n
for cont in range(0,m):
    x,y,c = map(int, input().split())
    debts[x-1] += c
    credit[y-1] += c

total = [0]*n
for cont in range(0,n):
    total[cont] = debts[cont]-credit[cont]

ris = 0
for n in total:
    if n > 0:
        ris += n

print(ris)
