__author__ = 'Данила'
(n, m) = map(int, input().split())
mat = [['' for i in range(m)] for j in range(n)]
for i in range(n):
    s = input().rstrip()
    for j in range(len(s)):
        mat[i][j] = s[j]
cnt = 0
for i in range(n - 1):
    for j in range(m - 1):
        mn = set()
        mn.add(mat[i][j])
        mn.add(mat[i + 1][j])
        mn.add(mat[i][j + 1])
        mn.add(mat[i + 1][j + 1])
        if 'f' in mn and 'a' in mn and ('c' in mn) and ('e' in mn):
            cnt += 1
print(cnt)
