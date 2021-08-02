n, k = map(int, input().split())
s = list(map(int, input().split()))
num = 0
w = []
w = [1 + 0.5 * (i - 1) for i in s]
cnt = sum(w[:k])
ans = cnt
for i in range(n - k):
    cnt -= w[i]
    cnt += w[i + k]
    if cnt > ans:
        ans = cnt
print(ans)
