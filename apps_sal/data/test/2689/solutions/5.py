# cook your dish here
s = input().strip()
s = s.replace('-', '+')
s = list(s.split('+'))
w = []
for i in range(len(s)):
    f = 0
    for j in range(1, len(s[i])):
        if not s[i][j].isalpha():
            w.append(s[i][:j])
            w.append(s[i][j:])
            f = 1
            break
    if not f:
        w.append(s[i])
#print(s, w)
res = ''
m = 1
for i in range(len(w)):
    if not w[i].isalpha():
        if w[i] != '':
            m = int(w[i])
    else:
        res += m * w[i]
        m = 1
if res == res[::-1]:
    print('Return')
else:
    print('Continue')
