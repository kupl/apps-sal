n,k = list(map(int,input().split()))
ai = list(map(int,input().split()))
bi = list(map(int,input().split()))
bi.sort()
j = k-1
for i in range(n):
    if ai[i] == 0:
        ai[i] = bi[j]
        j -= 1

ans = 0
for i in range(1,n):
    if ai[i-1] >= ai[i]:
        ans = 1
if ans  == 1:
    print("Yes")
else:
    print("No")

