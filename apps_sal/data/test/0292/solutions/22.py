(h, n) = input().split(' ')
h = int(h)
n = int(n)
s = 'l'
ans = 0
for i in range(h, 0, -1):
    if n > pow(2, i - 1):
        if s == 'l':
            ans += pow(2, i)
        else:
            ans += 1
        s = 'l'
        n -= pow(2, i - 1)
    else:
        if s == 'r':
            ans += pow(2, i)
        else:
            ans += 1
        s = 'r'
print(ans)
