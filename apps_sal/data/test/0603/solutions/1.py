(r, g, b) = map(int, input().split())
cr = r // 3
cg = g // 3
cb = b // 3
(a, b, c) = (r % 3, g % 3, b % 3)
cc = min(a, b, c)
if cc == 0 and a + b + c == 4:
    if a == 0 and cr > 0:
        cr -= 1
        cc += 2
    if b == 0 and cg > 0:
        cg -= 1
        cc += 2
    if c == 0 and cb > 0:
        cb -= 1
        cc += 2
print(cr + cg + cb + cc)
