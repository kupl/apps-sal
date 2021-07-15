line = input().split()
n = int( line[0])
m = int(line[1])
s = input()
t = input()
min = n + 1
A = []
for i in range(m-n+1):
    ii = i
    L = []
    k = 0 
    for j in range(len( s)):
        if ( t[ii] != s[j] ):
            L.append(j+1)
            k = k + 1
        ii = ii + 1
    if ( k < min ):
        min = k
        A = L
print(min)
for i in range(len(A)):
    print(A[i], end = " ")
print()

