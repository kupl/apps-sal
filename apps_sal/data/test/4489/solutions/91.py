N = int(input())
S = [input() for i in range(N)]
M = int(input())
T = [input() for i in range(M)]

answer = 0
for i in S:
    answer = max(answer, S.count(i) - T.count(i))
print(answer)
