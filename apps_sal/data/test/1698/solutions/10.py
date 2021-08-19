(n, k) = list(map(int, input().split()))
f = list(map(int, input().split()))
f = sorted(f)
i = 0
cnt = 0
for i in range(1, n + 1, k):
    cnt += (f[-i] - 1) * 2
print(cnt)
