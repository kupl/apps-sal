N, W = list(map(int, input().split()))
item = [tuple(map(int, input().split())) for _ in range(N)]

w1 = item[0][0]
V = [[] for _ in range(4)]
for w, v in item:
    V[w - w1].append(v)
for i in range(4):
    V[i].sort(reverse=True)

cnt = [0] * 4
for i in range(4):
    cnt[i] = len(V[i])

ans = 0
for i in range(cnt[0] + 1):
    S0 = sum(V[0][:i])
    W0 = i * w1
    for j in range(cnt[1] + 1):
        S1 = sum(V[1][:j])
        W1 = j * (w1 + 1)
        for k in range(cnt[2] + 1):
            S2 = sum(V[2][:k])
            W2 = k * (w1 + 2)
            for l in range(cnt[3] + 1):
                S3 = sum(V[3][:l])
                W3 = l * (w1 + 3)
                if W0 + W1 + W2 + W3 <= W:
                    ans = max(ans, S0 + S1 + S2 + S3)

print(ans)
