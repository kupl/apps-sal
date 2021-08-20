MOD = 10 ** 9 + 7


def I():
    return list(map(int, input().split()))


def find(s):
    r = []
    for i in s[::-1]:
        if i == '(':
            r.append(')')
    return ''.join(r) if len(r) == len(s) else False


def pre(s):
    k = [1]
    for i in s:
        if i == ')' and k[-1] == '(':
            k.pop()
        else:
            k.append(i)
    return ''.join(k[1:])


(n,) = I()
d = {'a': 0}
l = []
for i in range(n):
    s = input()
    s = pre(s)
    l.append(s)
    if not s:
        d['a'] += 1
    elif s in d:
        d[s] += 1
    else:
        d[s] = 1
count = 0
l.sort(key=lambda x: len(x))
for i in l:
    k = find(i)
    if i and i[0] != ')' and (k in d) and (d[k] > 0):
        count += 1
        d[k] -= 1
        d[i] -= 1
count += d['a'] // 2
print(count)
