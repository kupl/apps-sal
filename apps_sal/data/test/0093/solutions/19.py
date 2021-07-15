import copy
def g(s):
    ans = set()
    q = [s]
    while q:
        t = q.pop(0)
        for i in range(2):
            for j in range(2):
                if t[i][j] == 'X':
                    xx = copy.deepcopy(t)
                    xx[i][j], xx[i][1 - j] = xx[i][1 - j], xx[i][j]
                    k = ''.join([''.join(r) for r in xx])
                    if k not in ans:
                        ans.add(k)
                        q.append(xx)

                    xx = copy.deepcopy(t)
                    xx[i][j], xx[1 - i][j] = xx[1 - i][j], xx[i][j]
                    k = ''.join([''.join(r) for r in xx])
                    if k not in ans:
                        ans.add(k)
                        q.append(xx)

    return ans

t = []
t.append(list(input()))
t.append(list(input()))

r = []
r.append(list(input()))
r.append(list(input()))

print('YES' if (g(r) & g(t)) else 'NO')

