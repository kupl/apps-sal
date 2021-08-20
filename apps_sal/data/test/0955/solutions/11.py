n = int(input())
d = {}
for _ in range(n):
    s = input().split()
    p = int(s[0])
    s[1] = list(s[1])
    s[1].sort()
    s[1] = ''.join(s[1])
    if s[1] in d:
        d[s[1]] = min(d[s[1]], p)
    else:
        d[s[1]] = p


def get(s):
    if s in d:
        return d[s]
    return 10 ** 6


a = get('A')
b = get('B')
c = get('C')
ab = get('AB')
bc = get('BC')
ac = get('AC')
abc = get('ABC')
ans = min(a + b + c, a + bc, b + ac, c + ab, abc, ab + bc, ab + ac, ac + bc)
if ans < 10 ** 6:
    print(ans)
else:
    print(-1)
