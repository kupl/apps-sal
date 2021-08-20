from itertools import accumulate
(N, W) = map(int, input().split())
V0 = []
V1 = []
V2 = []
V3 = []
for i in range(N):
    (w, v) = map(int, input().split())
    if i == 0:
        w1 = w
        V0.append(v)
    elif w == w1:
        V0.append(v)
    elif w == w1 + 1:
        V1.append(v)
    elif w == w1 + 2:
        V2.append(v)
    else:
        V3.append(v)
V0.sort(reverse=True)
V1.sort(reverse=True)
V2.sort(reverse=True)
V3.sort(reverse=True)
CV0 = [0] + V0
CV0 = list(accumulate(CV0))
CV1 = [0] + V1
CV1 = list(accumulate(CV1))
CV2 = [0] + V2
CV2 = list(accumulate(CV2))
CV3 = [0] + V3
CV3 = list(accumulate(CV3))
ans = -float('inf')
for a in range(len(V0) + 1):
    for b in range(len(V1) + 1):
        for c in range(len(V2) + 1):
            for d in range(len(V3) + 1):
                if w1 * a + (w1 + 1) * b + (w1 + 2) * c + (w1 + 3) * d <= W:
                    sum_v = CV0[a] + CV1[b] + CV2[c] + CV3[d]
                    ans = max(ans, sum_v)
print(ans)
