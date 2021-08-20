def foo():
    s = input()
    d = {}
    for key in s:
        d[key] = d.get(key, 0) + 1
    return d


def f(s):
    d = {}
    for key in list(s.keys()):
        if ord(key) > ord('Z'):
            c = chr(ord(key) - ord('a') + ord('A'))
            d[c] = d.get(c, 0) + s[key]
        else:
            d[key] = d.get(key, 0) + s[key]
    return d


s = foo()
t = foo()
yr = 0
op = 0
for key in list(s.keys()):
    element = min(s[key], t.get(key, 0))
    yr += element
    s[key] -= element
    if t.get(key):
        t[key] -= element
s = f(s)
t = f(t)
for key in list(s.keys()):
    element = min(s[key], t.get(key, 0))
    op += element
    s[key] -= element
    if t.get(key):
        t[key] -= element
print(yr, op)
