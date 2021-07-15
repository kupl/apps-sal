from itertools import groupby as gb

N, I = map(int,input().split())
A = list(map(int,input().split()))
A = sorted(A)
l = []
G = gb(A)
for k, v in G:
    l.append(len(list(v)))

k = 100
while True:
    if N * k > 8 * I:
        k -= 1
    else:
        break
K = 2 ** k

NN = len(l)
if NN <= K:
    print(0)
    return

sm = sum(l[:K])
mx = sm

for i in range(K, NN):
    sm += l[i] - l[i - K]
    mx = max(mx, sm)

print(sum(l) - mx)
