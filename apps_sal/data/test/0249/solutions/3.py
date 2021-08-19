(n, l, x, y) = list(map(int, input().split()))
a = set(map(int, input().split()))
boy = False
girl = False
one = False
where = -1
for i in a:
    if i + x in a:
        boy = True
    if i + y in a:
        girl = True
    if i - x > 0 and i - x + y in a:
        one = True
        where = i - x
    if i + x < l and i + x - y in a:
        one = True
        where = i + x
    if i + x + y in a:
        one = True
        where = i + x
    if i - x - y in a:
        one = True
        where = i - x
if boy and girl:
    print(0)
if boy and (not girl):
    print(1)
    print(y)
if girl and (not boy):
    print(1)
    print(x)
if not boy and (not girl):
    if one:
        print(1)
        print(where)
    if not one:
        print(2)
        print(x, y)
