n = int(input())
A = list(map(int, input().split()))
mx = 0
tot = 0

for i in range(n):
    if(A[i] != mx + 1) :
        continue
    mx = A[i]
    tot += 1

if(tot == 0) :
    ans = -1
else :
    ans = n - tot
print(ans)
