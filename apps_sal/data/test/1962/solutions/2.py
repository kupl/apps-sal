T = input().split(' ')
n = int(T[0])
k = int(T[1])
l = int(T[2])
P = input().split(' ')
for i in range(n * k):
    P[i] = int(P[i])
P.sort()
a = 0
while a < n * k and P[a] - P[0] <= l:
    a+=1
if a < n:
    print(0)
else:
    tot = 0
    i = 0
    j = a
    for g in range(n-1, -1, -1):
        tot += P[i]
        i+=1
        j-=1
        for f in range(k-1):
            if j > g:
                i+=1
                j-=1
            else:
                break
    print(tot)

