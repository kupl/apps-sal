N, M = list(map(int, input().split()))
H = []
D = []
for i in range(M):
    d, h = list(map(int, input().split()))
    H.append(h)
    D.append(d)

res = max(max(H), H[M - 1] + N - D[M - 1])
res = max(res, H[0] + D[0] - 1)

for i in range(M - 1):
    dest = D[i + 1] - D[i]
    diff = abs(H[i + 1] - H[i])
    if diff > dest:
        res = float('inf')
        break
    else:
        res = max(res, (dest - diff) // 2 + max(H[i + 1], H[i]))

if res == float('inf'):
    print("IMPOSSIBLE")
else:
    print(res)
