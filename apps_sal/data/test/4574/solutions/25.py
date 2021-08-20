N = int(input())
A = list(map(int, input().strip().split()))
d = {}
for n in range(N):
    if d.get(A[n]) == None:
        d[A[n]] = 1
    else:
        d[A[n]] += 1
d = sorted(list(d.items()), reverse=True)
cnt = 0
ans = 0
for i in range(len(d)):
    if cnt == 0:
        if d[i][1] >= 4:
            ans = d[i][0] ** 2
            break
        elif d[i][1] >= 2:
            temp = d[i][0]
            cnt += 1
    elif d[i][1] >= 2:
        ans = temp * d[i][0]
        break
print(ans)
