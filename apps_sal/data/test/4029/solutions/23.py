s = input()[::-1]
t = len(s)


def g(c, i=0):
    return s.find(str(c), i) + 1 or 50


(i, f) = (g(0), g(5))
j = min(g(0, i), f)
m = i + j - 3 + (j < i)
j = min(g(2), g(7))
l = f + j - 3 + (j < f)
if f == t:
    i = t - 1
    while s[i - 1] == '0':
        l += 1
        i -= 1
m = min(m, l)
print((-1, m)[m < 40])
