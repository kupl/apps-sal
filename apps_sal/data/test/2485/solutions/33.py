h, w, n = map(int, input().split())
H = [0] * h
W = [0] * w
L = [(0, 0)] * n
for i in range(n):
    a, b = map(int, input().split())
    L[i] = (a, b)
    H[a - 1] += 1
    W[b - 1] += 1
h_max = max(H)
w_max = max(W)
ans = h_max + w_max
cnt = 0
for l in L:
    if H[l[0] - 1] == h_max and W[l[1] - 1] == w_max:
        cnt += 1
if H.count(h_max) * W.count(w_max) == cnt:
    ans -= 1
print(ans)
