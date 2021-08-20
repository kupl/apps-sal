s = list(input())
n = len(s)
ans = 0
for i in range(n):
    if s[i] in ['A', 'G', 'C', 'T']:
        s[i] = 'a'
for i in range(n):
    for j in range(i, n):
        flag = True
        for k in range(i, j + 1):
            if s[k] != 'a':
                flag = False
        if flag:
            ans = max([ans, j - i + 1])
print(ans)
