from collections import Counter
S = input()
N = len(S)
T = [0]
for i in range(N):
    p = int(S[-1 - i])
    T.append((T[-1] + pow(10, i, 2019) * p) % 2019)
ans = 0
U = dict(Counter(T))
for num in U:
    ans += U[num] * (U[num] - 1) // 2
print(ans)
