n = int(input())
s = input()
ans = int(n * (n - 1) / 2)
c = 0
for i in range(n):
    if s[i] == 'A':
        c += 1
    else:
        if c > 1:
            ans -= c - 1
        c = 0
c = 0
for i in range(n):
    if s[i] == 'B':
        c += 1
    else:
        if c > 1:
            ans -= c - 1
        c = 0
s = s[::-1]
c = 0
for i in range(n):
    if s[i] == 'A':
        c += 1
    else:
        if c > 1:
            ans -= c - 1
        c = 0
c = 0
for i in range(n):
    if s[i] == 'B':
        c += 1
    else:
        if c > 1:
            ans -= c - 1
        c = 0
c = 0
if s[0] == 'A':
    c += 1
for i in range(n):
    if s[i] == 'A':
        c += 1
    elif c >= 1:
        ans -= 1
        c = 0
c = 0
if s[0] == 'B':
    c += 1
for i in range(n):
    if s[i] == 'B':
        c += 1
    elif c >= 1:
        ans -= 1
        c = 0
print(ans)
