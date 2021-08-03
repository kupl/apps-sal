from itertools import*
s = input()
k = int(input())
l = len(s)
print(sorted(set(s[i:j] for i, j in combinations(range(l + 1), 2) if j - i <= k))[k - 1])
