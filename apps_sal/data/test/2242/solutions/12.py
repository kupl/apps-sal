from collections import Counter
S = input()
N = len(S)
l = [0] * (N + 1)
for i in range(N - 1, -1, -1):
    l[i] = (l[i + 1] + pow(10, N - i, 2019) * int(S[i])) % 2019
r = sum((m * (m - 1) // 2 for m in Counter(l).values()))
print(r)
