N = int(input())
m, *P = sorted([int(input()) for x in range(N)], reverse=True)

"""
m = P[N-1]
P = P[:N-1]
"""

print(sum(P) + m // 2)
