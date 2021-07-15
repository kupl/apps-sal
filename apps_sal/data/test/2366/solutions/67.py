from collections import Counter
n = int(input())
A = list(map(int, input().split()))
a = {}
ANS = 0
for x,y in Counter(A).items():
    if y >= 2: 
        a[x] = [y, (y*(y-1))//2]
        ANS += (y*(y-1))//2
for i in range(n):
    ans = ANS
    if A[i] in a:
        x = a[A[i]][0]-1
        ans -= a[A[i]][1]
        ans += (x*(x-1))//2
    print(ans)
