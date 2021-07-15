import sys
f = sys.stdin

n = int(f.readline().strip())

s = f.readline().strip()

v = ["vaporeon", "jolteon", "flareon", "espeon", "umbreon", "leafeon", "glaceon", "sylveon"]

for vi in v:
    t = True
    if n!=len(vi):
        t = False
        continue
    
    for l in range(len(s)):
        if s[l] != '.' and vi[l] != s[l]:
            t = False
            break
    
    if t:
        res = vi
        break

print(res)    
