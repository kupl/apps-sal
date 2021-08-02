n = int(input())
a = []
d = []
for i in range(2 * n - 2):
    b = input()
    a.append(b)
    if len(b) == n - 1:
        d.append(b)
s1 = d[0] + d[1][-1]
s2 = d[1] + d[0][-1]


def ans(s):
    l = ['' for _ in range(2 * n - 2)]
    for i in range(2 * n - 2):
        if l[i] != '': continue
        m1 = i
        m2 = -1
        for j in range(i + 1, 2 * n - 2):
            if len(a[j]) == len(a[i]):
                m2 = j
                break
        if s.startswith(a[i]) and s.endswith(a[j]):
            l[i] = 'P'
            l[j] = 'S'
        elif s.startswith(a[j]) and s.endswith(a[i]):
            l[j] = 'P'
            l[i] = 'S'
    if any(i == '' for i in l):
        return None
    return ''.join(l)


s = ans(s1)
if s:
    print(s)
else:
    print(ans(s2))
