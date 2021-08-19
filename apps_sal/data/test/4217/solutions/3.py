(n, m) = map(int, input().split())
l = [0] * m
for i in range(n):
    s = list(map(int, input().split()))
    for j in range(1, len(s)):
        l[s[j] - 1] += 1
print(l.count(n))
