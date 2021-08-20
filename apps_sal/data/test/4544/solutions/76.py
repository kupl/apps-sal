N = int(input())
A = list(map(int, input().split()))
ans = 0
cnt = [0] * (10 ** 5 + 10)
for i in range(N):
    cnt[A[i]] += 1
for i in range(0, 100000):
    sum = cnt[i] + cnt[i + 1] + cnt[i + 2]
    ans = max(ans, sum)
print(ans)
