n = int(input())
ans = 0
p = []
for i in range(n):
    p.append(list(input()))
    s = p[i].count('C')
    ans += s * (s - 1)
for i in range(n):
    col = 0
    for t in range(n):
        if p[t][i] == 'C':
            col += 1
    ans += col * (col - 1)
print(ans // 2)
