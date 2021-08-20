"""
import bisect
shop=int(input())
price=list(map(int,input().split()))
q=int(input())
price.sort()
for i in range(q):
            m=int(input())
            k=bisect.bisect_right(price,m,0,shop)
            print(len(price)-len(price[k:]))
"""
'\nimport math\nn,k=map(int,input().split())\nlis=[]\nfor i in range(n):\n            p,t=map(int,input().split())\n            lis.append([p,t])\nlis=sorted(lis,key=lambda x,y:(cmp(x[0],y[0]),cmp(y[1],x[1])),reverse=True)\nm=lis[k-1]\nprint(lis.count(m))\nprint(lis)\n'
n = int(input())
lis = input().split()
twos = lis.count('2')
ones = n - twos
if twos == 0 or ones == 0:
    print(' '.join(lis))
else:
    print('2 1' + ' 2' * (twos - 1) + ' 1' * (ones - 1))
