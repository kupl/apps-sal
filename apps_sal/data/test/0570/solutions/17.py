import sys
read=lambda:sys.stdin.readline().rstrip()
readi=lambda:int(sys.stdin.readline())
writeln=lambda x:sys.stdout.write(str(x)+"\n")
write=lambda x:sys.stdout.write(x)
a,b=map(int, read().split())
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
