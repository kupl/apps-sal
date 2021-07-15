from sys import stdin
n = int(stdin.readline())
a = [int(x) for x in stdin.readline().split()]

q = int(stdin.readline())

def gcd(a,b):
    while a != 0:
        a,b = b%a, a
    return b
    
totals = {}
new = {}

for x in a[::-1]:
    old = new
    new = {}
    for y in old:
        g = gcd(x,y)
        if g in new:
            new[g] += old[y]
        else:
            new[g] = old[y]
    if x in new:
        new[x] += 1
    else:
        new[x] = 1
    for y in new:
        if y in totals:
            totals[y] += new[y]
        else:
            totals[y] = new[y]
    
            


for x in range(q):
    c = int(stdin.readline())
    if c in totals:
        print(totals[c])
    else:
        print(0)

