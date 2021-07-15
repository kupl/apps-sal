n,k = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

answer = list()

for i in range(n//k):
    res = 0
    m = '1'+'0'*k
    m = int(m)-1
    q = str(b[i]) + '9' * (k-1)
    q = int(q)
    c = str(b[i]-1) + '9' * (k-1)
    c = int(c)
    c = max(c,-1)
    #print(m,q,c)
    res = (m//a[i]+1) - q//a[i] + c//a[i]
    answer.append(res)

resa = 1
#print(answer)
if sum(answer)==0:
    print(0)
else:
    for i in answer:
        resa = (resa*i)%1000000007
    print(resa)
