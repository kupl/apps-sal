def rotate(p, w, h):
    rot = [[] for i in range(w)]
    for i in range(w):
        for j in range(h):
            rot[i].append(p[j][i])
        rot[i] = list(reversed(rot[i]))
    return rot

def double():
    nonlocal mas, r
    p = 0
    for i in range(h):
        s = ''
        for j in r[i]:
            s += j * 2
        mas[p] = s
        mas[p + 1] = s
        p += 2   

def reverse():
    nonlocal r
    for i in range(h):
        r[i] = list(reversed(r[i]))    

w, h = map(int, input().split())
p = [[] for i in range(h)]
for i in range(h):
    s = input()
    for j in range(w):
        p[i].append(s[j])
r = rotate(p, w, h)
h, w = w, h
reverse()
mas = [['.' for i in range(w * 2)] for i in range(h * 2)]
double()
for i in range(h * 2):
    print(*mas[i], sep='')

