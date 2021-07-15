N = int(input())
P = list(map(int,input().split()))
search, count, flag, ans, pans = 1, 0, 0, [], []
for i in range(N):
    x = P[i]
    if x == search:
        ans += pans[::-1]
        if i < N-1:
            if flag == 0:
                print(-1)
                return
            search, count, flag, pans = i+1, 0, 0, []
            P[i], x = P[i-1], P[i-1]
        
    if x != search:
        if flag == 1:
            print(-1)
            return
        if x > count+search+1:
            flag = 1
        pans.append(i+1)
        count += 1
        
for k in ans:
    print(k)
