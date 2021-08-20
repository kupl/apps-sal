n = int(input())
s = input()
o = 0
c = 0
n = len(s)
for i in range(n):
    if s[i] == '(':
        o += 1
    else:
        c += 1
if n % 2 != 0:
    print(0)
    quit()
if abs(o - c) > 2:
    print(0)
    quit()
t = 0
count = 0
ans = 0
for i in range(n):
    if s[i] == '(':
        count += 1
    else:
        count -= 1
    if count < -2:
        t = 1
if t == 1:
    print(0)
    quit()
ind = n - 1
count = 0
if o > c:
    ind = -1
    for i in range(n):
        if s[i] == '(':
            count += 1
        else:
            count -= 1
        if count < 0:
            print(0)
            quit()
        if count < 2:
            ind = i
    for i in range(ind + 1, n):
        if count > 0 and s[i] == '(':
            ans += 1
        if s[i] == '(':
            count += 1
        else:
            count -= 1
        if count < 0:
            t = 1
elif c > o:
    for i in range(n):
        if s[i] == '(':
            count += 1
        else:
            count -= 1
        if count < 0:
            ind = i
            break
    for i in range(ind + 1):
        if s[i] == ')':
            ans += 1
else:
    print(0)
    quit()
print(ans)
