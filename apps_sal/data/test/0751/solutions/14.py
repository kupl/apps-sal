n, m = list(map(int,input().split()))
group = list(map(int,input().split()))

b = 0


tot = 0
for i in range(n):
    tot += group[i]
    if tot > m :
        b += 1
        tot = group[i]
    elif tot == m :
        b += 1
        tot = 0
    if i == n-1 and tot != 0 :
        b += 1
print(b)

