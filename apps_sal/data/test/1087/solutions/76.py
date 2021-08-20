import sys
input = sys.stdin.readline
(N, K) = map(int, input().split())
A = list(map(int, input().split()))
B = [0] * 40
for a in A:
    for i in range(40):
        if a & 1 << i:
            B[i] += 1
X = [0] * 40
for i in range(40):
    if B[i] <= N / 2:
        X[i] = 1
bitK = list(map(int, list(bin(K)[2:].zfill(40)[::-1])))
ans = 0
for i in range(40):
    if bitK[i] == 1:
        ans += N - B[i] << i
    else:
        ans += B[i] << i
for k in range(40):
    if bitK[k] == 0:
        continue
    total = 0
    leqK = False
    for i in range(39, -1, -1):
        if leqK:
            if X[i] == 1:
                total += N - B[i] << i
            else:
                total += B[i] << i
        elif i == k:
            total += B[i] << i
            leqK = True
        elif bitK[i] == 1:
            total += N - B[i] << i
        else:
            total += B[i] << i
    ans = max(total, ans)
print(ans)
