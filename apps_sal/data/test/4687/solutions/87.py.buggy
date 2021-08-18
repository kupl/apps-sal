N, K = map(int, input().split())

bucket = [0] * (10 ** 5 + 1)
for _ in range(N):
    a, b = map(int, input().split())
    bucket[a] += b

cnt = 0
for i, c in enumerate(bucket):
    if c == 0:
        continue
    cnt += c
    if cnt >= K:
        print(i)
        return
