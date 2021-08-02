a = list(map(int, input().split()))
s = input()
d = []
for i in range(26):
    d.append({})
sm = 0
k = 0
for x in s:
    n = ord(x) - ord('a')
    k += d[n].get(sm, 0)
    sm += a[n]
    d[n][sm] = d[n].get(sm, 0) + 1
print(k)
