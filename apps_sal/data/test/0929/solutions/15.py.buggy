H, W = list(map(int, input().split()))
A = []

for i in range(H):
    a = list(map(int, input().split()))
    if i % 2:
        a.reverse()
    A.extend(a)

ans = []
for i in range(H * W - 1):
    if A[i] % 2:
        ans.append(i)
        A[i + 1] += 1

N = len(ans)
print(N)


def move(m):
    y1, x1 = divmod(m, W)
    y2, x2 = divmod(m + 1, W)
    y1 += 1
    y2 += 1
    if m // W % 2:
        x1 = W - x1
    else:
        x1 += 1
    if (m + 1) // W % 2:
        x2 = W - x2
    else:
        x2 += 1
    return (y1, x1, y2, x2)


for i in range(N):
    print((*move(ans[i])))
