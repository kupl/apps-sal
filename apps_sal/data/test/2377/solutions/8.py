n, h = map(int, input().split())
AB = [(list(map(int, input().split()))) for _ in range(n)]

A = []
B = []
for a, b in AB:
    A.append(a)
    B.append(b)

max_A = max(A)
C = sorted([b for b in B if b >= max_A], reverse=True)

cnt = 0
for c in C:
    h -= c
    cnt += 1
    if h <= 0:
        print(cnt)
        return

atack = h // max_A
cnt += atack
h -= atack * max_A
if h <= 0:
    print(cnt)
else:
    print(cnt + 1)
