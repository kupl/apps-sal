(N, K) = list(map(int, input().split()))
A = list(map(int, input().split()))
b = 1 << 63
X = 0
ans = 0
for i in range(64):
    cnt = 0
    for a in A:
        if a & b:
            cnt += 1
    if N >= cnt * 2 and X ^ b <= K:
        X ^= b
        ans += (N - cnt) * b
    else:
        ans += cnt * b
    b >>= 1
print(ans)
