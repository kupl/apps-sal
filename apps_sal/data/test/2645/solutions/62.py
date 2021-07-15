s = str(input())
n = len(s)

L = []
c = 0
ans = 0
for i in range(n):
    if c-1 >= 0:
        if s[i] == 'g':
            ans += 1
            c -= 1
        else:
            c -= 1
    else:
        if s[i] == 'g':
            c += 1
        else:
            ans -= 1
            c += 1
print(ans)
