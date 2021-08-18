A, B, X = map(int, input().split())
s = 1
e = 1000000000


def price(x):
    return x * A + len(str(x)) * B


if price(s) > X:
    print(0)
    return
if price(e) <= X:
    print(e)
    return

while e > s + 1:
    tmp = (s + e) // 2
    if price(tmp) <= X:
        s = tmp
    else:
        e = tmp
print(s)
