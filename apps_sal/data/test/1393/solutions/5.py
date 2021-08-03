u = input()
v = input()
a = [0 for i in range(200)]
b = [0 for i in range(200)]
m = 0
n = 0
d = ord('a') - ord('A')
for i in u:
    a[ord(i)] += 1
for i in v:
    b[ord(i)] += 1
for i in range(ord('A'), ord('Z') + 1):
    r = min(a[i], b[i]) + min(a[i + d], b[i + d])
    n += r
    m += min(a[i] + a[i + d], b[i] + b[i + d]) - r
print(n, m)
