from collections import Counter
N = int(input())
S = Counter([input() for _ in range(N)])
M = int(input())
T = Counter([input() for _ in range(M)])

ans = 0

for word, count in S.items():
    temp = count - T[word]
    ans = max(ans, temp)
print(ans)
