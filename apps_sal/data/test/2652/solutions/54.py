from scipy.sparse.csgraph import minimum_spanning_tree
from scipy.sparse import csr_matrix

N = int(input())
A = []
for i in range(N):
    x, y = list(map(int, input().split()))
    A.append((i, x, y))

length, frm, to = [], [], []
path_set = set()


def path(axis):
    A.sort(key=lambda x: x[axis])
    for i in range(N - 1):
        if (A[i][0], A[i + 1][0]) in path_set:
            continue
        length.append(min(abs(A[i][1] - A[i + 1][1]),
                          abs(A[i][2] - A[i + 1][2])))
        frm.append(A[i][0])
        to.append(A[i + 1][0])
        path_set.add((A[i][0], A[i + 1][0]))


path(1)
path(2)
matr = csr_matrix((length, (frm, to)), shape=(N, N))

T = minimum_spanning_tree(matr).astype(int)
print((sum(T.data)))
