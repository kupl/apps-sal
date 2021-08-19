from collections import Counter
S = list(map(int, list(input())))
A = [0]
for (i, s) in enumerate(S[::-1]):
    A.append((A[-1] + s * pow(10, i, 2019)) % 2019)
print(sum([v * (v - 1) // 2 for v in list(Counter(A).values())]))
