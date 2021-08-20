(N, T) = map(int, input().split())
time = list(map(int, input().split()))
cnt = 0
for i in range(1, N):
    cnt += min(T, time[i] - time[i - 1])
print(cnt + T)
