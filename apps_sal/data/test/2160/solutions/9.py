n, k = map(int, input().split())
x = [int(i) for i in input().split()]

first = [int(k + 1) for _ in range(n + 1)]
last = [int(-1) for _ in range(n + 1)]

for i in range(k):
    first[x[i]] = min(first[x[i]], i)
    last[x[i]] = max(last[x[i]], i)

cnt = 0
for i in range(1, n + 1):
    if last[i] == -1:
        cnt += 1
    if i + 1 <= n:
        if last[i] < first[i + 1]:
            cnt += 1
        if last[i + 1] < first[i]:
            cnt += 1

print(cnt)
