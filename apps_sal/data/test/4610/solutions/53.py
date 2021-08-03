N, K = list(map(int, input().strip().split()))
A = list(map(int, input().strip().split()))

d = {}

for n in range(N):
    if d.get(A[n]) == None:
        d[A[n]] = 1
    else:
        d[A[n]] += 1

dn = sorted(list(d.items()), key=lambda x: x[1])

if K >= len(d):
    print((0))
else:
    cnt = 0
    ans = 0
    for n in range(len(dn)):
        ans += dn[n][1]
        cnt += 1
        if cnt == len(d) - K:
            break
    print(ans)
