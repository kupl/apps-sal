N, M = list(map(int, input().split()))
AB = [list(map(int, input().split())) for _ in range(N)]

AB.sort(key=lambda x: (-x[1], -x[0]))
memo = [0] * (10**5 + 1)
work = [float('inf')] * (10**5 + 1)
noMore = float('inf')
ans = 0
for a, b in AB:
    if a < noMore:
        flag = 1
        for idx in range(min(M - a, work[a]), -1, -1):
            if memo[idx] == 0:
                ans += b
                memo[idx] = 1
                flag = 0
                work[a] = idx
                break
        if flag == 1:
            noMore = a

print(ans)
