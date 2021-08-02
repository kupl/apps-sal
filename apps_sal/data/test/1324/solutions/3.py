a, b, c, d = map(int, input().split())
res = 0
s = input()
n = len(s)
for i in range(n):
    if s[i] == '1':
        res += a
    if s[i] == '2':
        res += b
    if s[i] == '3':
        res += c
    if s[i] == '4':
        res += d
print(res)
