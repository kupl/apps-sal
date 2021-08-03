N, W = map(int, input().split())
A = []
W1, W2, W3, W4 = [], [], [], []
for i in range(N):
    w, v = map(int, input().split())
    if i == 0:
        a = w
    A.append((v, w))
    if w - a == 0:
        W1.append(v)
    elif w - a == 1:
        W2.append(v)
    elif w - a == 2:
        W3.append(v)
    else:
        W4.append(v)


W1, W2, W3, W4 = sorted(W1)[::-1], sorted(W2)[::-1], sorted(W3)[::-1], sorted(W4)[::-1]

l1, l2, l3, l4 = len(W1), len(W2), len(W3), len(W4)
ans = 0
for i in range(l1 + 1):
    for j in range(l2 + 1):
        for k in range(l3 + 1):
            for l in range(l4 + 1):
                value = sum(W1[:i]) + sum(W2[:j]) + sum(W3[:k]) + sum(W4[:l])
                if a * i + (a + 1) * j + (a + 2) * k + (a + 3) * l <= W:
                    ans = max(ans, value)
print(ans)
