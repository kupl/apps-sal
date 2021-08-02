n = int(input())
price = []
vita = []
dmin = {}
dmin['A'] = 9999999
dmin['B'] = 9999999
dmin['C'] = 9999999
dmin['AB'] = 9999999
dmin['AC'] = 9999999
dmin['BC'] = 9999999
dmin['ABC'] = 9999999
for i in range(n):
    p, v = input().split()
    # price.append(int(p))
    p = int(p)
    v = ''.join(sorted(v))
    if dmin[v] > p:
        dmin[v] = p
    vita.append((p, v))
th1 = dmin['A'] + dmin['B'] + dmin['C']
th2 = dmin['A'] + dmin['BC']
th3 = dmin['B'] + dmin['AC']
th4 = dmin['C'] + dmin['AB']
th5 = dmin['ABC']
th6 = dmin['AB'] + dmin['BC']
th7 = dmin['AC'] + dmin['BC']
th8 = dmin['AB'] + dmin['AC']
res = min(th1, th2, th3, th4, th5, th6, th7, th8)
if res == 9999999:
    print(-1)
else:
    print(res)
