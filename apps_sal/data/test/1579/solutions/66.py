import numpy as np
from scipy.sparse import csr_matrix, csgraph
import sys
input = sys.stdin.readline
U = 10 ** 5
n = int(input())
xy = np.array([input().split() for _ in range(n)], dtype=np.int32)
graph = csr_matrix((np.ones(n, dtype=np.bool), (xy[:, 0], U + xy[:, 1])), (2 * U + 1, 2 * U + 1))
(_, component) = csgraph.connected_components(graph)
x_cnt = np.bincount(component[:U + 1], minlength=2 * U + 2)
y_cnt = np.bincount(component[U + 1:], minlength=2 * U + 2)
pts_cnt = np.bincount(component[xy[:, 0]], minlength=2 * U + 2)
answer = (x_cnt * y_cnt - pts_cnt).sum()
print(answer)
