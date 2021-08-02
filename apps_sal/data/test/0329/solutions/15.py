s = input()
k = s
l = s
d = s
r = s
k = k.replace("n", "")
l = l.replace("i", "")
d = d.replace("t", "")
r = r.replace("e", "")
n, i, t, e = 0, 0, 0, 0
n = len(s) - len(k)
i = len(s) - len(l)
t = len(s) - len(d)
e = len(s) - len(r)
x = 0
if n - 3 >= 0 and i - 1 >= 0 and t - 1 >= 0 and e - 3 >= 0:
    g = "nineteen"
    n -= 3
    i -= 1
    t -= 1
    e -= 3
    x += 1
    while n - 2 >= 0 and i - 1 >= 0 and t - 1 >= 0 and e - 3 >= 0:
        n -= 2
        i -= 1
        t -= 1
        e -= 3
        x += 1
print(x)
