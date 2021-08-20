n = int(input())
s = input()
v = ''
h = ''
vs = {'U', 'D'}
hs = {'L', 'R'}
ans = 1
for i in s:
    if i in vs:
        if v == '':
            v = i
        elif v != i:
            v = i
            ans += 1
            h = ''
    elif h == '':
        h = i
    elif h != i:
        h = i
        ans += 1
        v = ''
print(ans)
