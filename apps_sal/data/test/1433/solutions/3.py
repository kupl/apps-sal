(n, m) = list(map(int, input().split()))
d = []
res = 0
for i in range(n):
    s = input()
    if s.count('1') != 0:
        l = s.find('1')
        r = s.rfind('1')
        res += s[:l].count('0')
        res += s[r + 1:].count('0')
        res += s[l + 1:r].count('0') * 2
    d.append(s)
for i in range(0, m * 2, 2):
    ss = ''
    for k in range(n):
        ss += d[k][i]
    if ss.count('1') != 0:
        l = ss.find('1')
        r = ss.rfind('1')
        res += ss[:l].count('0')
        res += ss[r + 1:].count('0')
        res += ss[l + 1:r].count('0') * 2
print(res)
