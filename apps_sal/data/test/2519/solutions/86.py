(N, K) = map(int, input().split())
p = list(map(int, input().split()))
s = sum(p[:K])
ss = []
ss.append(s)
for i in range(N - K):
    s = s - p[i] + p[i + K]
    ss.append(s)
print(K + (max(ss) - K) / 2)
