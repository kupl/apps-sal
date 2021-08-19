# 060_D
n, W = map(int, input().split())
w1, w2, w3, w4 = [], [], [], []
w, v = map(int, input().split())
w1.append(v)
for _ in range(n - 1):
    a, b = map(int, input().split())
    if a == w:
        w1.append(b)
    if a == w + 1:
        w2.append(b)
    if a == w + 2:
        w3.append(b)
    if a == w + 3:
        w4.append(b)

for w_ in [w1, w2, w3, w4]:
    w_.sort(reverse=True)

ans = 0
for i in range(0, len(w1) + 1):
    for j in range(0, len(w2) + 1):
        for k in range(0, len(w3) + 1):
            res = W - (i * w + j * (w + 1) + k * (w + 2))
            if res < 0:
                continue
            tmp = sum(w1[:i]) + sum(w2[:j]) + sum(w3[:k]) + sum(w4[:res // (w + 3)])
            ans = max(tmp, ans)

print(ans)
