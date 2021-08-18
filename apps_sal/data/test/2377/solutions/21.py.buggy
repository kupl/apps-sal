N, H = [int(_) for _ in input().split()]

A = []
B = []
for _ in range(N):
    a, b = [int(_) for _ in input().split()]
    A.append(a)
    B.append(b)

a = max(A)
cnt = 0

for b in sorted(B, reverse=True):
    if b < a:
        break
    H -= b
    cnt += 1

    if H <= 0:
        print(cnt)
        return

cnt += H // a
if H % a != 0:
    cnt += 1
print(cnt)
