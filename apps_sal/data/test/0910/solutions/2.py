n, a, b = [int(x) for x in input().split()]
s = [ [0 for j in range(b)] for i in range(a) ]
x, y = 1, 2
i, j = 0, 0
last = 0
while i < a and (x <= n or y <= n):
    parity = True
    while j < b and (x <= n or y <= n):
        if parity and x<=n:
            s[i][j] = x  
            x += 2
        elif not parity: 
            s[i][j] = y
            y += 2
        parity = not parity
        last = max(last, s[i][j])
        j += 1
    i += 1
    j  = 0
    x, y = y, x
if last == n:
    print('\n'.join(' '.join(str(x) for x in ln) for ln in s))
else:
    print(-1)

