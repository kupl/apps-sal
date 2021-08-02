from functools import cmp_to_key


def compare(f, u):
    if f + u < u + f:
        return -1
    elif f + u == u + f:
        return 0
    else:
        return 1


n = int(input())
s = []
for i in range(n):
    s.append(input())
print(''.join(sorted(s, key=cmp_to_key(compare))))
