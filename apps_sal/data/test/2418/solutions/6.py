n = int(input())
aaa = list(map(int, input().split()))
diff = []
score = 0
prv = 0
for a in aaa:
    d = a - prv
    diff.append(d)
    if d > 0:
        score += d
    prv = a
buf = [(score + min(0, diff[0]) + 1) // 2]

q = int(input())
for _ in range(q):
    l, r, x = list(map(int, input().split()))
    l -= 1
    dl1 = diff[l]
    diff[l] += x
    dl2 = diff[l]
    score += max(0, dl2) - max(0, dl1)

    if r < n:
        dr1 = diff[r]
        diff[r] -= x
        dr2 = diff[r]
        score += max(0, dr2) - max(0, dr1)

    buf.append((score + min(0, diff[0]) + 1) // 2)

print('\n'.join(map(str, buf)))
