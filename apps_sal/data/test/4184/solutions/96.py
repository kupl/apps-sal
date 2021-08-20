N = int(input())
W = map(int, input().split())
W = list(W)
diffs = []
for n in range(1, N):
    w1 = W[:n]
    w2 = W[n:]
    su_w1 = sum(w1)
    su_w2 = sum(w2)
    diff = abs(su_w1 - su_w2)
    diffs.append(diff)
print(min(diffs))
