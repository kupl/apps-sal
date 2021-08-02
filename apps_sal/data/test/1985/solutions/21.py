(k, n) = (int(i) for i in input().split())

a = []
prev = 0
for i in input().split():
    prev = prev + int(i)
    a.append(prev)

b = [int(i) for i in input().split()]
kands = set()
for i in a:
    kands.add(b[0] - i)
b = set(b)
cnt = 0
for i in kands:
    cur = set()
    for j in a:
        cur.add(i + j)
    if b <= cur:
        cnt += 1
print(cnt)
