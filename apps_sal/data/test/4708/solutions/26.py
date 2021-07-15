from sys import stdin
input = stdin.readline

N = int(input())
K = int(input())
X = int(input())
Y = int(input())

if N <= K:
    cost = N * X
else:
    cost = K * X + (N - K) * Y

print(cost)
