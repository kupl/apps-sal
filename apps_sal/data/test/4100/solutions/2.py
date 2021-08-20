(N, K, Q) = list(map(int, input().split()))
ans = [K for _ in range(N)]
for i in range(Q):
    A = int(input())
    ans[A - 1] += 1
ans = list([x - Q for x in ans])
for j in ans:
    if j <= 0:
        print('No')
    else:
        print('Yes')
