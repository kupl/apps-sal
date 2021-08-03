n = int(input())

a = list(map(int, input().split()))

a = a + a

#print( a )

mid = n // 2

best = 99999999999999999999999

for i in range(n):
    sub = a[i:i + n]
    #print( sub )
    d = sum(sub)
    best = min(best, d)
    s = 0

    #print( d, s )
    for j in range(n):
        s += sub[j]
        d -= sub[j]

        diff = abs(s - d)
        best = min(best, diff)

print(best)
