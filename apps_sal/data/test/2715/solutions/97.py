# K回の操作
# N = 50とする
# 0,1,2,3,4...N - 1の数列に対して左からi番目にNを足し、それ以外から1を引く操作
# K // N回の操作をすると、1回あたり全項目に1が足される。

import sys
readline = sys.stdin.readline

K = int(readline())
N = 50

A = [i for i in range(N)]
A = list(map(lambda x: x + (K // N), A))
rest = K % N
for i in range(rest):
    A[i] += N
    for j in range(N):
        if i != j:
            A[j] -= 1

print(N)
print(*A)
