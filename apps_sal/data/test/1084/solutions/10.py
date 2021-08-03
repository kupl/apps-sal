n, m = list(map(int, input().split()))
s = [input() for _ in range(n)]
l = []

for i in range(n):
    se = set()

    for j in range(m):
        if s[i][j] == '#':
            se.add(j)

    for li in l:
        if len(se & li) != 0 and se != li:
            print('No')
            return

    l.append(se)

print('Yes')
