from collections import Counter
N = list(input())
M = [0]
S = 0
K = 1
ans = 0

for i in range(len(N)):
    S += int(N[-i-1])*K
    S %= 2019

    K *= 10
    K %= 2019
    M.append(S)

P = Counter(M)
for i in range(2020):ans+=P[i]*(P[i]-1)//2
print(ans)

