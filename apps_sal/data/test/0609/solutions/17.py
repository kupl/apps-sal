n = int(input())
res = 'YES'
s = list(input())
chk = s[0]
nul = s[1]
if s[0] != chk or s[n-1] != chk or s[0] == nul or s[n-1] == nul:
    res = 'NO'
s[0] = nul
s[n-1] = nul
if not all([x == nul for x in s]):
    res = 'NO'
if res == 'YES':
    for j in range(1, n):
        s = list(input())
        if s[j] != chk or s[n-1-j] != chk or s[j] == nul or s[n-1-j] == nul:
            res = 'NO'
        s[j] = nul
        s[n-1-j] = nul
        if not all([x == nul for x in s]):
            res = 'NO'
print(res)

