n,k,q = map(int, input().split())
a = list(map(int, input().split()))

ans=10**15
for i in range(n):
    x=a[i]
    y_cand=[]
    lis=[]

    for j in range(n):
        if a[j] < x:
            if len(lis)-k+1 >= 0:
                lis.sort()
                y_cand.extend(lis[:len(lis)-k+1])
            lis=[]
        else:
            lis.append(a[j])

    if len(lis)-k+1 >= 0:
        lis.sort()
        y_cand.extend(lis[:len(lis)-k+1])

    if len(y_cand) >= q:
        y_cand.sort()
        y = y_cand[q-1]
        ans = min(ans,abs(x-y))

print(ans)
