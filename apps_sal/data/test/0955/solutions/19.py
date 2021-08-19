n = int(input())
d = {'A': 10000000000.0, 'B': 10000000000.0, 'C': 10000000000.0, 'AB': 10000000000.0, 'BC': 10000000000.0, 'AC': 10000000000.0, 'ABC': 10000000000.0}
for i in range(n):
    (a, b) = input().split()
    a = int(a)
    b = ''.join(sorted(list(b)))
    d[b] = min(d.get(b), a)
k = min(d['A'] + d['B'] + d['C'], d['AB'] + d['BC'], d['BC'] + d['AC'], d['AB'] + d['AC'], d['ABC'], d['BC'] + d['A'], d['AB'] + d['C'], d['AC'] + d['B'])
if k >= 10000000000.0:
    print(-1)
else:
    print(k)
