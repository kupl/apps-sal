
def is_lexigraphic(s):
    for i in range(len(s) - 1):
        if s[i] > s[i + 1]:
            return False
    return True


def I(): return list(map(int, input().split()))


n, m = I()
a = [input() for i in range(n)]
mn = m
columns = list(zip(*a))
for i in range(m):
    curCol = columns[i]
    if not is_lexigraphic(curCol):
        continue
    l = []
    for j in range(n - 1):
        if curCol[j] == curCol[j + 1]:
            l.append(j)
    x = 0
    for k in range(i + 1, m):
        if any([columns[k][a] > columns[k][a + 1] for a in l]):
            x += 1
        elif any([columns[k][a] == columns[k][a + 1] for a in l]):
            l = [a for a in l if columns[k][a] == columns[k][a + 1]]
        else:
            break
    mn = min(x + i, mn)
print(mn)
