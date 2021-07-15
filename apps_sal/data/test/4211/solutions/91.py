n = int(input())
bn = [int(num) for num in input().split()]
 
an = [0]*n
an[0] = bn[0]
an[n-1] = bn[n-2]
for i in range(1,n-1):
    s = min(bn[i],bn[i-1])
    an.append(s)
    
print(sum(an))
