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
        else:
            if v != i:
                v = i
                ans += 1
                h = ''
    else:
        if h == '':
            h = i
        else:
            if h != i:
                h = i
                ans += 1
                v = ''
print(ans)
