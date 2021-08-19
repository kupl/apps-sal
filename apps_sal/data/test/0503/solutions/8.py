s = 0
m = {}
o = {}
(n, k) = map(int, input().split())
l = list(map(int, input().split()))
for a in l:
    o[a / k] = m[a / k] = m[a] = o[a] = 0
for a in l:
    if a % k == 0:
        s += m[a / k]
        m[a] += o[a / k]
    o[a] += 1
print(s)
