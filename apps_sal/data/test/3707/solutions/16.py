n,t,k,d=[int(x) for x in input().split()]
c=n//k+(n%k>0)
print('YES' if (c-1)*t>d else 'NO')
