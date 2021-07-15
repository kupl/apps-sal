n=int(input())
d = {'A':float('Inf'), 'B':float('Inf'), 'C':float('Inf'), 'AB':float('Inf'), 'AC':float('Inf'), 'BC':float('Inf'), 'ABC':float('Inf')}
for i in range(n):
    r = input().split()
    c = int(r[0])
    s = r[1]
    s = ''.join(sorted([x for x in s]))
    d[s] = min(d[s], c)
ans = min(d['ABC'], d['A']+d['BC'], d['AB']+d['BC'],d['AB']+d['AC'], d['AC']+d['BC'], d['B']+d['AC'], d['C']+d['AB'], d['A']+d['B']+d['C'])
if ans < float('Inf'):
    print(ans)
else:
    print(-1)
