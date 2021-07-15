3.5

N = int(input())
A = input()

L = []
cpt = 1
ret = 0

for i in range(1, len(A)):
    if A[i] == A[i-1]:
        cpt += 1
    else:
        L.append(cpt)
        if A[i] == "S":
            ret = max(ret, cpt)
            
        cpt = 1

L.append(cpt)
if A[-1] == "G":
    ret = max(ret, cpt)

if ret == 0:
    print("0")
    return

if A[0] == "G":
    cur = True
else:
    cur = False

for i in range(0, len(L)):
    if not cur:
        if L[i] == 1 and (i+3 < len(L) or i-3 >= 0):
            new = 1
            if i > 0:
                new += L[i-1]
            if i < len(L)-1:
                new += L[i+1]

            ret = max(ret, new)

        if L[i] == 1 and i > 0 and i < len(L)-1:
            ret = max(ret, L[i-1] + L[i+1])
                
        if i > 0 and i+1 < len(L):
            ret = max(ret, L[i-1]+1)

        if i < len(L)-1 and i-1 >= 0:
            ret = max(ret, L[i+1]+1)
    
    cur = not cur

print(ret)

