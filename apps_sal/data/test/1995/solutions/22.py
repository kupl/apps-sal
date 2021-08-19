import sys
s = list(sys.stdin.readline())
s2 = list(s)
numQ = int(sys.stdin.readline())
for i in range(numQ):
    ls = sys.stdin.readline().split()
    l = int(ls[0]) - 1
    r = int(ls[1]) - 1
    k = int(ls[2])
    diff = r - l + 1
    for j in range(0, diff):
        newpos = (j + k) % diff + l
        s2[newpos] = s[j + l]
    s = list(s2)
sys.stdout.write(''.join(s2))
