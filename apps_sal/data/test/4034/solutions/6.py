n = int(input())
s = input()
f = [0 for _ in range(26)]
res = [1 for _ in range(n)]
for i in range(n):
    c = ord(s[i]) - ord('a')
    for j in range(c + 1, 26):
        res[i] = max(res[i], f[j] + 1)
    f[c] = max(f[c], res[i])
maxres = max(res)
if maxres <= 2:
    print('YES')
    for i in res:
        print(i - 1, end='')
else:
    print('NO')
