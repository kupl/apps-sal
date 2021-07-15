n = int(input())
for i in range(n):
    k = int(input())
    used = [0]*k
    a = list(map(int, input().split()))
    p = 0
    ans = [0]*k
    for i in range(k):
        if a[i] != p:
            ans[i] = a[i]
            used[a[i]-1] = 1
        p = a[i]
    t = 0
    flag = 0
    for i in range(k):
        if ans[i] == 0:
            while used[t] == 1 and t < a[i]:
                t +=1
            if t == a[i]:
                flag = 1
                break
            else:
                used[t] = 1
                ans[i] = t+1
    if flag == 1:
        print(-1)
    else:
        print(*ans)

