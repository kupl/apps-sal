
(l,r,a) = input().split()
l = int(l)
r = int(r)
a = int(a)

dif = abs(r-l)
if (r< l):

    r += min(a, l-r)
    a -= min(a, dif)
else:
    l += min(a, r-l)
    a -= min(a, dif)


if (a > 0):
    print(2*(r + a//2))
else:
    print(2*min(r,l))

