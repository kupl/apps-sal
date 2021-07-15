def ii():
    return int(input())
def mi():
    return map(int, input().split())
def li():
    return list(mi())

n, m = mi()
s = input().strip()
t = input().strip()
ok = 0
if '*' not in s:
    ok = s == t
else:
    i = s.index('*')
    l = s[:i]
    r = s[i+1:]
    if t.startswith(l):
        t = t[i:]
        if t.endswith(r):
            ok = 1
print('YES' if ok else 'NO')
