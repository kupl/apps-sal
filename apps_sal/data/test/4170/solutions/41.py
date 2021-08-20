N = int(input())
H = list(map(int, input().split()))
cnt = [0] * N
now = 0
for i in range(1, N):
    if H[i] <= H[i - 1]:
        now += 1
        cnt[i] = now
    else:
        now = 0
print(max(cnt))
