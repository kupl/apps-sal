N = int(input())
(S1, S2) = [list(map(int, input().split())) for i in range(2)]
S = 0
for i in range(N):
    S = max(S, sum(S1[:i + 1]) + sum(S2[i:]))
print(S)
