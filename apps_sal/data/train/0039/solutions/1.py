from sys import stdin,stderr
def rl():
    return [int(w) for w in stdin.readline().split()]

t, = rl()
for _ in range(t):
    a,b,p = rl()
    s = stdin.readline().rstrip()
    r = 1
    t = ''
    for i in range(len(s)-1,0,-1):
        if s[i-1] != t:
            t = s[i-1]
            p -= a if t == 'A' else b
            if p < 0:
                r = i+1
                break
    print(r)

