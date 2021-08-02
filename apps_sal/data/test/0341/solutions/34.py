n, k = map(int, input().split())
r, s, p = map(int, input().split())
t = input()

c = [''] * n
ans = 0
for i in range(n):
    if t[i] == 'r':
        rsp = 'p'
        point = p
    elif t[i] == 's':
        rsp = 'r'
        point = r
    elif t[i] == 'p':
        rsp = 's'
        point = s

    if i >= k and c[i - k] == rsp:
        rsp = ''
        point = 0

    c[i] = rsp
    ans += point
print(ans)
