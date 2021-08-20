import itertools
N = int(input())
d = {'M': 0, 'A': 0, 'R': 0, 'C': 0, 'H': 0}
for _ in range(N):
    s = input()
    if s[0] in d:
        d[s[0]] += 1
a = list(itertools.combinations('MARCH', 3))
ans = 0
for l in a:
    ans += d[l[0]] * d[l[1]] * d[l[2]]
print(ans)
