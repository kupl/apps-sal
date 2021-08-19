(N, K) = map(int, input().split())
data = list(map(int, input().split()))
cnt = 0
for i in range(len(data)):
    if data[i] >= K:
        cnt += 1
print(cnt)
