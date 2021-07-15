n, m = list(map(int, input().split()))
s = input()
si = []

for ch in s:
    if ch == '0':
        si.append(0)
    else:
        si.append(1)

ptr = n
ret = []

while ptr > 0:
    for me in range(m, -1, -1):
        if me == 0:
            print((-1))
            return
        if ptr - me < 0:
            continue
        if si[ptr-me] == 0:
            ret.append(me)
            ptr -= me
            break

ret.reverse()

print((' '.join(map(str, ret))))

