n, m = map(int, input().split())
d = [{'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0} for i in range(m)]
for i in range(n):
    s = input()
    for j in range(len(s)):
        d[j][s[j]] += 1
array = list(map(int, input().split()))
s = 0
for i in range(m):
    ma = 0
    for el in d[i]:
        if d[i][el] > ma:
            ma = d[i][el]
    s += ma * array[i]
print(s)
