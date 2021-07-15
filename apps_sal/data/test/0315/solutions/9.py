n, k = map(int, input().split())
l = list(map(int, input().split()))
cnt = 0
for i in range(n - 1):
    if l[i] + l[i + 1] < k:
        cnt += k - l[i] - l[i + 1]
        l[i + 1] += k - l[i] - l[i + 1]
print(cnt)
print(' '.join(map(str, l)))
