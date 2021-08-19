from itertools import combinations
s = [int(input()) for _ in [0] * 6]
k = s.pop()
r = 'Yay!'
for (i, j) in combinations(s, 2):
    if j - i > k:
        r = ':('
        break
print(r)
