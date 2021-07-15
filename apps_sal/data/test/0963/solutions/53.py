q = 998244353

N, K = map(int, input().split())

S = []
for _ in range(K):
    S.append(list(map(int, input().split())))

result = [0]*N
result[0] = 1
result[1] = -1

for i in range(N - 1):
    for l, r in S:
        if i + l < N:
            result[i + l] = (result[i + l] + result[i]) % q
            if i + r + 1 < N:
                result[i + r + 1] = (result[i + r + 1] - result[i]) % q
    result[i + 1] = (result[i] + result[i + 1]) % q

print(result[-1])
