H, W, K = list(map(int, input().split()))

S = [input() for _ in range(H)]

ans = 10**10
for i in range(2**(H - 1)):
    rel = [0 for h in range(H)]
    a, b = 0, 0
    for h in range(H - 1):
        if i >> h & 1:
            b += 1
        rel[h + 1] = b

    a += b

    cnt = [0 for j in range(b + 1)]
    for w in range(W):
        for h in range(H):
            if S[h][w] == '1':
                cnt[rel[h]] += 1

        OK = True
        for j in range(b + 1):
            if cnt[j] > K:
                OK = False
                break

        if OK:
            continue

        a += 1
        cnt = [0 for j in range(b + 1)]
        for h in range(H):
            if S[h][w] == '1':
                cnt[rel[h]] += 1

        OK2 = True
        for j in range(b + 1):
            if cnt[j] > K:
                OK2 = False
                break

        if OK2:
            continue
        a = 10**10
        break
    ans = min(ans, a)
print(ans)
