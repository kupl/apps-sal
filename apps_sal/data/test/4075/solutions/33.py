import itertools

N,M = list(map(int, input().split()))
A = []

for m in range(M):
    a = list(map(int, input().split()))
    A.append(a[1:])

P = list(map(int, input().split()))

S = itertools.product([0,1],repeat=N)
ans = 0

for s in S:
    flag = True
    for i in range(M):
        temp = 0
        for a in A[i]:
            temp += s[a-1]
        if temp % 2 != P[i]:
            flag = False
    if flag == True:
        ans += 1

print(ans)

