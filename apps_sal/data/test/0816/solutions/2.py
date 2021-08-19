(n, x) = list(map(int, input().split()))
a = list(map(int, input().split()))
M = max(a) + 1
cnt = [0 for _ in range(M)]
for num in a:
    cnt[num] += 1
res = 0
for num in range(1, M):
    if cnt[num] > 0:
        s = num ^ x
        if M > s >= num:
            res += cnt[s] * cnt[num] if s != num else (cnt[s] - 1) * cnt[s] // 2
print(res)
