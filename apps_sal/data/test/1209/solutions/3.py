n = int(input())
a = [input() for _ in range(n)]
ans = []
ch = [False] * n
cur = -1
for i in a:
    cur += 1
    if '.' in i:
        curi = i.split('.')
        if curi[1].count('0') == len(curi[1]):
            ans.append(int(curi[0]))
            continue
        ch[cur] = True
        if curi[0][0] == '-':
            ans.append(int(curi[0]) - 1)
        else:
            ans.append(int(curi[0]))
    else:
        ans.append(int(i))
curs = sum(ans)
for i in range(n):
    if curs < 0 and ch[i]:
        curs += 1
        ans[i] += 1
print(*ans, sep='\n')
