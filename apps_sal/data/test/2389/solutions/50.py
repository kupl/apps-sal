n,a,b,c = list(map(int, input().split()))
m = {'A':a, 'B':b, 'C':c}

ss = [input() for _ in range(n)]


ans = []
def _t(s0, s1):
    m[s0] = m[s0] + 1
    m[s1] = m[s1] - 1
    ans.append(s0)


if a+b+c == 0:
    print('No')
    return


elif a+b+c == 1:
    for k, v in list(m.items()):
        if v == 1:
            o = k

    for s in ss:
        if o not in s:
            print('No')
            return
        o = s.strip(o)
        ans.append(o)

elif a+b+c == 2:
    for i, s in enumerate(ss):
        if m[s[0]] + m[s[1]] == 0:
            print('No')
            return
        if m[s[0]] > m[s[1]]:
            _t(s[1], s[0])
        elif m[s[0]] < m[s[1]]:
            _t(s[0], s[1])
        else:
            if i < len(ss)-1 and s[0] in ss[i+1]:
                _t(s[0], s[1])
            else:
                _t(s[1], s[0])

else:
    for s in ss:
        if m[s[0]] + m[s[1]] == 0:
            print('No')
            return
        if m[s[0]] > m[s[1]]:
            _t(s[1], s[0])
        else:
            _t(s[0], s[1])

print('Yes')
for a in ans:
    print(a)

