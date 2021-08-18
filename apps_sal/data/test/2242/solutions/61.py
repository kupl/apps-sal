from collections import Counter

S = input()[::-1]

X = [0]


for i, s in enumerate(S):
    X.append((X[-1] + int(s) * pow(10, i, 2019)) % 2019)


C = Counter(X)

ans = 0
for v in list(C.values()):
    ans += v * (v - 1) // 2

print(ans)
