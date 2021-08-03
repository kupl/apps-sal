n = int(input())
m = list(map(int, input().split()))
for i in range(n):
    if(m[i] >= 0):
        m[i] = -m[i] - 1
if(n % 2 == 0):
    print(" ".join(map(str, m)))
else:
    mi = 0
    ind = -1
    for i in range(n):
        if(mi > m[i] and m[i] != -1):
            mi = m[i]
            ind = i
    if(ind != -1):
        m[ind] = -m[ind] - 1
    else:
        m[0] = 0
    print(" ".join(map(str, m)))
