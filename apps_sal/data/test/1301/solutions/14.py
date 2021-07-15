# -- code beginning
n = int(input())
s = input()
vrs = ["vaporeon", "jolteon", "flareon", "espeon", "umbreon", "leafeon", "glaceon", "sylveon"] 
def match(a, b):
    if len(a) != len(b): return False
    for (ac, bc) in zip(a, b):
        if ac == '.' or bc == '.': continue
        elif ac != bc: return False
    return True

for i in vrs:
    if match(s, i):
        print(i)
        break

# -- code end

