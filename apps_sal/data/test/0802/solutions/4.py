n = int(input())
s = input()
q = len(set(s))
d = {}
count = 0
best = 999999999
j = 0
for i in range(n):
    if s[i] not in d:
        d[s[i]] = 0
        count += 1
    d[s[i]] += 1
    if count == q:
        while d[s[j]] > 1:
            d[s[j]] -= 1
            j += 1
        best = min(best, i - j + 1)
print(best)
