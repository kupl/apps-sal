import numpy as np
from scipy.sparse.csgraph import maximum_bipartite_matching
from scipy.sparse import csr_matrix
import sys
input = sys.stdin.readline


N = int(input())

X = []
Y = []
for i in range(N):
    X.append([int(i) for i in input().split()])

for i in range(N):
    Y.append([int(i) for i in input().split()])

data = []
for i in range(len(X)):
    for j in range(N):
        if X[i][0] < Y[j][0] and X[i][1] < Y[j][1]:
            data.append([i, j, 1])


if not data:
    print(0)
    return

edge = np.array(data, dtype=np.int64).T
# graph = csr_matrix((edge[2], (edge[:2] - 1)), (V, V))
graph = csr_matrix((edge[2], (edge[:2])), (len(X), len(Y)))           # 番号のデクリメントが不要な場合

matching = maximum_bipartite_matching(graph, perm_type="column")

print(sum(d != -1 for d in matching))
