n,A,B = map(int, input().split())
L = list(map(int, input().split()))
a = L[0]
S = sum(L)
L = sorted(L[1:],reverse=True)
count = 0
for i in L:
    if a/S*A>=B:
        break
    else:
        S-=i
        count+=1
print(count)
