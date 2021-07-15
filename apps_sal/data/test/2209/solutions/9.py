import functools

n = int(input())

t = [input() for i in range(n)]


def compare(s1, s2):
    if (s1.count('s') * len(s2)) < (s2.count('s') * len(s1)):
        return 1
    else:
        return -1


t = sorted(t, key=functools.cmp_to_key(compare))
s = ''.join(t)

c = 0
z = 0

for char in s:
    if char == 's':
        c += 1
    elif char == 'h':
        z += c
print(z)

