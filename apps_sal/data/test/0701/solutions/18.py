import sys
try:
    f = open("input.txt")
except IOError:
    f = sys.stdin
s = f.readline().rstrip()
t = f.readline().rstrip()
needTree = False
_s = s[:]
for c in t:
    if c in _s:
        _s = _s[:_s.index(c)] + _s[_s.index(c) + 1:]
    else:
        needTree = True
if needTree:
    print("need tree")
else:
    if not t in s:
        if len(s) > len(t):
            j = 0
            both = False
            for i in range(len(t)):
                while j < len(s) and s[j] != t[i]:
                    j += 1
                if j >= len(s):
                    both = True
                j += 1
            if both:
                print("both")
            else:
                print("automaton")
        else:
            print("array")
    else:
        print("automaton")
