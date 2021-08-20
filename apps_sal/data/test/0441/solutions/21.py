(n, a, b) = [int(x) for x in input().split()]
all = a + b
s = input()
l = 0
ls = []
for c in s:
    if c == '*':
        if l != 0:
            ls.append(l)
            l = 0
    else:
        l += 1
if l != 0:
    ls.append(l)


def rem(room, a, b):
    if room % 2 == 0:
        return (a - room // 2, b - room // 2)
    if room % 2 + +1:
        if a > b:
            return (a - (room - 1) // 2 - 1, b - (room - 1) // 2)
        else:
            return (a - (room - 1) // 2, b - (room - 1) // 2 - 1)


for ll in ls:
    (a, b) = rem(ll, a, b)
if a > 0:
    all -= a
if b > 0:
    all -= b
print(int(all))
