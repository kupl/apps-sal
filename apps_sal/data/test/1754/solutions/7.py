n, m, k = list(map(int, input().split()))
p = list(map(int, input().split()))
s = list(map(int, input().split()))
c = list(map(int, input().split()))

d = {}
for i in s:
    d[i] = 0

for i in range(len(s)):
    d[s[i]] = max(d[s[i]], p[i])

k = 0

for i in c:
    if d[s[i - 1]] > p[i - 1]:
        k += 1

print(k)
