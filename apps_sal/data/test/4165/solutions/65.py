N = int(input())
L = list(map(int, input().split()))
ans = True
for i in range(N):
    sum = 0
    for j in range(N):
        if i == j:
            continue
        else:
            sum += L[j]
    if L[i] >= sum:
        ans = False
if ans == True:
    print('Yes')
else:
    print('No')
