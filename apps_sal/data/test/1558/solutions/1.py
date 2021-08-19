__author__ = 'PrimuS'
(n, r, a) = (int(x) for x in input().split())
marks = [[0, 0]] * n
s = 0
for i in range(n):
    ss = input()
    marks[i] = [int(x) for x in ss.split()]
    s += marks[i][0]
if s / n >= a:
    print(0)
else:
    x = a * n - s

    def ccmp(b):
        return b[1]
    marks.sort(key=ccmp)
    i = 0
    res = 0
    while x > 0:
        y = min(x, r - marks[i][0])
        x -= y
        res += marks[i][1] * y
        i += 1
    print(res)
