"""
https://atcoder.jp/contests/abc131/submissions/6086380
"""
import os
import sys
import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import connected_components
if os.getenv('LOCAL'):
    sys.stdin = open('_in.txt', 'r')
sys.setrecursionlimit(2147483647)
INF = float('inf')
N = int(sys.stdin.readline())
(X, Y) = list(zip(*[list(map(int, sys.stdin.readline().split())) for _ in range(N)]))
PAD = 10 ** 5 + 1
X = np.array(X)
Y = np.array(Y) + PAD
graph = csr_matrix(([True] * N, (X, Y)), shape=(PAD * 2, PAD * 2))
(_, components) = connected_components(graph)
x_cnt = np.bincount(components[:PAD], minlength=PAD * 2)
y_cnt = np.bincount(components[PAD:], minlength=PAD * 2)
print((x_cnt * y_cnt).sum() - N)
