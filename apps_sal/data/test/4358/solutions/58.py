N = int(input())
(m, *P) = sorted([int(input()) for x in range(N)], reverse=True)
'\nm = P[N-1]\nP = P[:N-1]\n'
print(sum(P) + m // 2)
