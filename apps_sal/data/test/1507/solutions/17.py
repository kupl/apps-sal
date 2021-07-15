n, k = list(map(int, input().split()))
p = input()
ls, nlaps = [], 0
for i in range(65, 91):
    if chr(i) in p:
        start = p.index(chr(i))
        end = p.rfind(chr(i))
        ls.append((start,'start'))
        ls.append((end,'end'))
ls = list(sorted(ls, key=lambda x: x[0]))
# print(ls)
maxl = 0
for i,x in enumerate(ls):
    if x[1] == 'start':
        nlaps += 1
    else:
        nlaps -= 1
    maxl = max(maxl, nlaps)
if k >= maxl:
    print('NO')
else:
    print('YES')
    


