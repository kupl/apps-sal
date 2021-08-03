from scipy.sparse import*
H, *S = open(0)
H, W, *A = map(int, H.split())
for i in range(m := H * W):
    A += [m * 2, h := i // W, I := m * 3, m * 2, w := i % W + m, I] * ((c := S[h][w - m]) == 'S') + [h, I, I, w, I, I] * (c == 'T') + [h, w, 1, w, h, 1] * (c > 'T')
print([-1, f := csgraph.maximum_flow(csr_matrix((A[2::3], (A[::3], A[1::3])), [I + 1] * 2), m * 2, I).flow_value][f < I])
