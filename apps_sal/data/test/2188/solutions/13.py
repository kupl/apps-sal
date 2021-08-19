n = int(input())
d = {}
d['+'] = []
d['-'] = []
for _ in range(n):
    (a, b) = list(map(int, input().split()))
    if a < b:
        d['+'].append([b, _])
    else:
        d['-'].append([b, _])
d['+'] = sorted(d['+'], key=lambda x: x[0], reverse=True)
d['-'] = sorted(d['-'], key=lambda x: x[0])
s = ''
if len(d['+']) > len(d['-']):
    print(len(d['+']))
    for x in d['+']:
        s += str(x[1] + 1) + ' '
else:
    print(len(d['-']))
    for x in d['-']:
        s += str(x[1] + 1) + ' '
print(s)
