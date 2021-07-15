n, p, k = map(int, input().split())

pages = [str(i) for i in range(1, n+1)]

left = 0
if p-k-1>=0:left=p-k-1
elif k>p: left = 0
else:left=p-k

res = [' '.join(pages[left:p-1]), '(' + str(p) + ')',  ' '.join(pages[p:p+k])]

if p-k-1>0: res.insert(0,'<<')

if p+k<n: res.append('>>')

print(' '.join(res).strip())
