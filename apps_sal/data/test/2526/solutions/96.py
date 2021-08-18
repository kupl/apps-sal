from collections import deque

X, Y, A, B, C = map(int, input().split())
Q_A = list(map(int, input().split()))
Q_B = list(map(int, input().split()))
Q_C = list(map(int, input().split()))


Q_A = sorted(Q_A, reverse=True)[:X]
Q_B = sorted(Q_B, reverse=True)[:Y]
Q_C = sorted(Q_C, reverse=True)

cand = Q_A + Q_B + Q_C

cand = sorted(cand, reverse=True)
print(sum(cand[:(X + Y)]))
