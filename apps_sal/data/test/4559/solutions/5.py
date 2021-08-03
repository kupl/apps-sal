N = int(input())
A = list(map(int, input().split()))

if 0 in A:
    print(0)
    return
else:
    flag = True
    prd = 1
    A.sort(reverse=True)
    for i in range(N):
        prd *= A[i]
        if prd > 10**18:
            flag = False
            break
if flag:
    print(prd)
else:
    print(-1)
