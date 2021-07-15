N = int(input())
*A, = list(map(int, input().split()))
cnt = [0] * (N+1)
for a in A:  cnt[a] += 1
ans = 0
for c in cnt:
    ans += c*(c-1)//2
for a in A:
    r = 1 - cnt[a]
    print((ans + r))

