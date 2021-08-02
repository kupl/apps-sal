n, m = map(int, input().split())
s = [False] * n
t = [False] * n
for i in range(m):
    a, b = map(int, input().split())
    if a == 1:
        s[b - 1] = True
    if b == n:
        t[a - 1] = True
for i in range(n):
    if s[i] == True and t[i] == True:
        print('POSSIBLE')
        return
print('IMPOSSIBLE')
