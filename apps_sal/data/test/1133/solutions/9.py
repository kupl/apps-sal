n = int(input())


inp = [input() for i in range(n)]

gets = []

for line in inp:
    dt = {}
    for c in line:
        if c == ' ':
            continue
        if c in dt:
            dt[c] += 1
        else:
            dt[c] = 1
    ans = -1
    if len(dt) > 2:
        continue
    gets.append(dt)

lets = 'abcdefghijklmnopqrstuvwxyz'

ans = -1
for c1 in lets:
    for c2 in lets:
        if c2 <= c1:
            continue
        cans = 0
        for l in gets:
            failed = False
            for ch in l:
                if ch not in (c1, c2):
                    failed = True
            if failed:
                continue
            cans += sum(l.values())
        if cans > ans:
            ans = cans

print(ans)

