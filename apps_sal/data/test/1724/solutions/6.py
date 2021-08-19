n = int(input())
a = list(map(int, input().split()))
b = [0] + a
for i in range(1, n + 1):
    b[i] += b[i - 1]
t = input()
(s, m, i) = (0, 0, t.rfind('1'))
while i >= 0:
    d = b[i] + s
    if d > m:
        m = d
    if d + a[i] < m:
        break
    s += a[i]
    i = t[:i].rfind('1')
print(max(m, s))
