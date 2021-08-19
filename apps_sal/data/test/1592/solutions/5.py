(pt, s, vs) = (0, 0, 0)
for i in range(int(input())):
    (t, c) = map(int, input().split())
    s = max(s - (t - pt), 0) + c
    vs = max(vs, s)
    pt = t
print(pt + s, vs)
