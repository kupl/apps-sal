c = []
for i in range(3):
    tmp = input()
    c.append(tmp)
ans = ''
for i in range(3):
    ans += c[i][i]
print(ans)
