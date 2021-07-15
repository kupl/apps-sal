n , k , c = map(int,input().split())

s = input()

L = []
R = []

i = 0
j = n-1



while i<n and len(L)<k :
    if s[i] == "o" :
        L.append(i)
        i += c
    i += 1

while j>-1 and len(R)<k :
    if s[j] == "o" :
        R.append(j)
        j -= c
    j -= 1

R.reverse()

for x in range(k):
    if R[x] == L[x]:
        print(R[x]+1)
