M=10**9+7
r=tuple(tuple((j-k)*9%13for j in range(10))for k in range(13))
d=[1]+[0]*12
for c in input():
    if c>'9':
        d=[sum(d[j]for j in k)%M for k in r]
    else:
        d=[d[(int(c)-k)*9%13]for k in range(13)]
print(d[5])
