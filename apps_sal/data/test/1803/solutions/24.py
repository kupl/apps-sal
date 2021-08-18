import sys
3


def deb(*a): pass


_ = sys.stdin.readline()

birds = sys.stdin.readline().split(" ")
birds[-1] = birds[-1].strip("\n")

_ = sys.stdin.readline()

shoot_rec = []
for l in sys.stdin.readlines():
    l = l.split(" ")
    l[1] = l[1].strip("\n")
    shoot_rec.append(l)

lines = []
for n in birds:
    n = int(n)
    lines.append(n)

deb(lines)


for line, bird in shoot_rec:
    deb(line, bird)

    line = int(line) - 1
    bird = int(bird)

    if line != 0:
        lines[line - 1] += bird - 1

    if line != len(lines) - 1:
        lines[line + 1] += lines[line] - bird

    lines[line] = 0

    deb(lines)


deb("
for i in lines:
    print(i)
