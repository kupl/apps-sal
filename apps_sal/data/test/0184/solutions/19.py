l, r, a = map(int, input().split())
l, r = min(l, r), max(l, r)
f = min(r-l, a)
l += f
a -= f
o = l*2 + (a // 2) * 2
print(o)
