H, W, D = list(map(int, input().split()))
A = [list(map(int, input().split())) for _ in range(H)]
inv_A = [(0, 0)] * (H * W + 1)
for y, a in enumerate(A):
    for x, a_ in enumerate(a):
        inv_A[a_] = (y, x)
C = [0] * D
c = 0
for i in range(D, H * W + 1):
    y1, x1 = inv_A[i]
    y2, x2 = inv_A[i - D]
    C.append(abs(y1 - y2) + abs(x1 - x2) + C[i - D])
Ans = []
Q = int(input())
for _ in range(Q):
    l, r = list(map(int, input().split()))
    Ans.append(C[r] - C[l])
print(("\n".join(map(str, Ans))))
