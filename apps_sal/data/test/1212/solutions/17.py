n,k=list(map(int,input().split()))

z=[int(x) for x in input().split()]

pref=[0]
for i in range (1,n+1):
    pref.append(z[i-1]+pref[i-1])

##print (pref[:])
minsum=1000000000
minind=1

for j in range (1,n-k+2):
    if (pref[j+k-1]-pref[j-1]<minsum):
        minsum=pref[j+k-1]-pref[j-1]
        minind=j
    else:
        continue


print (minind)

