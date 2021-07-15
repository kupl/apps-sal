def go(s, t):
    sb = None
    si = 0
    for i in range(len(t)):
        if t[i] == s[si]:
            si += 1
            if si == 1:
                sb = (i,)
            if si == len(s):
                sb += (i,)
                return sb
    return None

s = input()
t = input()

si = 0
f = go(s, t)
s = [x for x in reversed(s)]
t = [x for x in reversed(t)]
l = go(s, t)

print((len(t) - l[1] - 1) - f[1] if f and l and (len(t) - l[1] - 1) - f[1] > 0 else 0)
