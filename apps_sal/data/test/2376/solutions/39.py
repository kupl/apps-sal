from itertools import accumulate
N, W = map(int, input().split())
w1, w2, w3, w4 = [], [], [], []
w, v = map(int, input().split())
w1.append(v)
for _ in range(N - 1):
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

w1 = [0] + w1
w1 = list(accumulate(w1))
w2 = [0] + w2
w2 = list(accumulate(w2))
w3 = [0] + w3
w3 = list(accumulate(w3))
w4 = [0] + w4
w4 = list(accumulate(w4))


ans = 0
for a in range(len(w1)):
    for b in range(len(w2)):
        for c in range(len(w3)):
            for d in range(len(w4)):
                wei = w * a + (w + 1) * b + (w + 2) * c + (w + 3) * d
                val = w1[a] + w2[b] + w3[c] + w4[d]
                if wei <= W:
                    ans = max(val, ans)

print(ans)
