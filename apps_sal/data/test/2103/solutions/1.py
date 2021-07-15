from sys import stdin,stderr
def rl():
    return [int(w) for w in stdin.readline().split()]

n, = rl()
a = rl()

a_set = set(a)
free = 0
prev = 0
b = []
for cur in a:
    if cur != prev:
        b.append(prev)
        if free == prev:
            free += 1
        prev = cur
    else:
        while free in a_set:
            free += 1
        b.append(free)
        free += 1
print(*b)

