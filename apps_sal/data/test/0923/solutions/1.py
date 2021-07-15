import sys

n = int(input())
a = list(map(int,input().split()))
for i in range(n+1) :
          for j in range(n) :
                    if j%2 : a[j]-=1
                    else : a[j]+=1
                    a[j]%=n
          if a==list(range(n)) :
                    print('Yes')
                    return
print('No')

