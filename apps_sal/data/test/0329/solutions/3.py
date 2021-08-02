J = str(input())
N = J.count('n')
I = J.count('i')
T = J.count('t')
E = J.count('e')
N = (N - 1) // 2
E = E // 3
if N > 0:
    M = min(N, I, T, E)
else:
    M = 0
print(M)
