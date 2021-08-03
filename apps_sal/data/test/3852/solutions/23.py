N = int(input())
A = list(map(int, input().split()))

ans = []
mx = max(A)
mi = min(A)

if mx * mi < 0:
    if abs(mi) > abs(mx):
        x = A.index(mi)
        for y in range(N):
            if y == x:
                continue
            A[y] += mi
            ans.append((x, y))
    else:
        x = A.index(mx)
        for y in range(N):
            if x == y:
                continue
            A[y] += mx
            ans.append((x, y))

for i in range(N - 1)[::(-1)**(min(A) < 0)]:
    l, r = A[i], A[i + 1]

    if l > r:
        if r >= 0:
            A[i + 1] += l
            ans.append((i, i + 1))
        elif l <= 0:
            A[i] += r
            ans.append((i + 1, i))

print((len(ans)))
for x, y in ans:
    print((x + 1, y + 1))

if list(sorted(A)) != A:
    print(A)
    1 / 0
