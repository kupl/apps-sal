import string
n = input()
a = list(input().split())


def rt(s):
    al = string.ascii_lowercase
    d = set()
    for l in s:
        d.add(l)
    return ''.join(sorted(list(d)))


s = set()
for w in a:
    s.add(rt(w))
print(len(s))
