import sys


def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


n = int(input())
s = input()
ambiguity = list(map(int, input().split()))
s_a = [y for y in list(zip([x for x in s], ambiguity)) if y[0] in 'hard']
if len(s_a) < 4:
    print(0)
    quit()
l = len(s_a) + 1
h = [0] * l
ha = [0] * l
har = [0] * l
hard = [0] * l
last_a = -1
last_r = -1
last_d = -1
for (i, (c, a)) in enumerate(s_a):
    if c == 'h':
        h[i] = a + h[i - 1]
    else:
        h[i] = h[i - 1]
    if c == 'a':
        ha[i] = min(h[i], a + ha[last_a])
        last_a = i
    else:
        ha[i] = ha[i - 1]
    if c == 'r':
        har[i] = min(ha[i], a + har[last_r])
        last_r = i
    else:
        har[i] = har[i - 1]
    if c == 'd':
        hard[i] = min(har[i], a + hard[last_d])
        last_d = i
    else:
        hard[i] = hard[i - 1]
eprint(h)
eprint(ha)
eprint(har)
eprint(hard)
print(hard[-2])
