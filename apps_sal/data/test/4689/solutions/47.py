#!/usr/local/bin/python3
# https://atcoder.jp/contests/abc160/tasks/abc160_c

K, N = list(map(int, input().split()))
A = list(map(int, input().split()))

dist = []
for i in range(N - 1):
    dist.append(A[i + 1] - A[i])
dist.append(K - A[-1] + A[0])

print((K - max(dist)))
