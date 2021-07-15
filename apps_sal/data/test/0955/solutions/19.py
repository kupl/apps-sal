n=int(input())
d={'A':10e9,'B':10e9,'C':10e9,'AB':10e9,'BC':10e9,'AC':10e9,'ABC':10e9}
for i in range(n):
    a,b=input().split()
    a=int(a)
    b=''.join(sorted(list(b)))
    d[b]=min(d.get(b),a)
k=min(d['A']+d['B']+d['C'],d['AB']+d['BC'],d['BC']+d['AC'],d['AB']+d['AC'],d['ABC'],d['BC']+d['A'],d['AB']+d['C'],d['AC']+d['B'])
if k>=10e9:
    print(-1)
else:
    print(k)

