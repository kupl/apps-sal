import sys
def read(): return sys.stdin.readline().rstrip()
def readi(): return int(sys.stdin.readline())
def writeln(x): return sys.stdout.write(str(x) + "\n")
def write(x): return sys.stdout.write(x)


a, b = map(int, read().split())
toggle = True
c = 1
while True:
    if toggle:
        a -= c
    else:
        b -= c
    if a < 0:
        writeln("Vladik")
        break
    if b < 0:
        writeln("Valera")
        break
    c += 1
    toggle = not toggle
