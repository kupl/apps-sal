N = int(input())
a = list(map(int, input().split()))
cnt = [[0] * (N + 1) for i in range(2)]
b = [0] * N
for i in range(N):
    b[i] = bin(a[i]).count('1')
num = 0
suf = 0
cnt[0][N] = 1
for i in range(N - 1, -1, -1):
    s = 0
    ma = 0
    suf += b[i]
    num += cnt[suf & 1][i + 1]
    for j in range(i, min(N, i + 65)):
        s += b[j]
        ma = max(ma, b[j])
        if ma * 2 > s and s % 2 == 0:
            num -= 1
    cnt[0][i] = cnt[0][i + 1]
    cnt[1][i] = cnt[1][i + 1]
    if suf & 1:
        cnt[1][i] += 1
    else:
        cnt[0][i] += 1
print(num)
