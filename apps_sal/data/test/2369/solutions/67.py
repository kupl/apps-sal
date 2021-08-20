(N, K) = map(int, input().split())
lis = list(map(int, input().split()))
sort_lis = sorted(lis)
p = 10 ** 9 + 7
fac_lis = [[0] for i in range(N)]
fac_lis[0] = 1
max_ans = 0
min_ans = 0
for i in range(1, N):
    fac_lis[i] = fac_lis[i - 1] * (i + 1) % p


def combi(n, k):
    if n == k:
        return 1
    else:
        return fac_lis[n - 1] * pow(fac_lis[k - 1], p - 2, p) * pow(fac_lis[n - k - 1], p - 2, p) % p


for i in range(K - 1, N):
    max_ans += sort_lis[i] * combi(i, K - 1)
    max_ans %= p
for i in range(N - K + 1):
    min_ans += sort_lis[i] * combi(N - (i + 1), K - 1)
    min_ans %= p
ans = (max_ans - min_ans) % p
print(ans)
