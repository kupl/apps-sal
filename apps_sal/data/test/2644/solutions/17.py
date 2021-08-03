N = int(input())
P = list(map(int, input().split()))
search, before, count, flag, ans, pans = 1, 0, 0, 0, [], []
for i in range(N):
    x = P[i]
    if x == search:
        if i < N - 1 and flag == 0:
            print(-1)
            return
        ans += pans[::-1]
        before, search, count, flag, pans = search, i + 1, 0, 0, []
        P[i], x = P[i - 1], P[i - 1]
    if x != search:
        if flag == 1:
            print(-1)
            return
        if x == count + search + 1:
            flag = 0
        if x > count + search + 1:
            flag = 1
        pans.append(i + 1)
        count += 1
    # print(i,x,pans)
print('\n'.join(map(str, ans)))
