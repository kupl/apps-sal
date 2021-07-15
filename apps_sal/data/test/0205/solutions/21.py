from decimal import Decimal

list_int_input = lambda inp: list(map(int, inp.split()))
int_input = lambda inp: int(inp)
string_to_list_input = lambda inp: list(inp)

n,b=list(map(int,input().split()))
import math
facts=[]
sqt=int(math.sqrt(b))
for i in range(2,sqt+1):
    j=0
    while b%i==0:
        j+=1
        b=int(Decimal(b)/Decimal(i))
    if j>0:
        facts.append((i, j))
    if b==1:
        break
if b!=1:
    facts.append((b,1))
summ=10**18
for i in facts:
    num=i[0]
    times=i[1]
    cnt=0
    while int(n/num)!=0:
        cnt+=int(Decimal(n)/Decimal(num))
        num*=i[0]
    summ=min(summ,int(Decimal(cnt)/Decimal(times)))
print(summ)


