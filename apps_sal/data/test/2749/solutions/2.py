(H, W) = map(int, input().split())
N = int(input())
A = list(map(int, input().split()))
A.insert(0, 0)
ans = [[-1 for _ in range(W)] for _ in range(H)]
color = 1
for i in range(H):
    for j in range(W):
        if A[color] == 0:
            color += 1
        A[color] -= 1
        ans[i][j] = color
for i in range(H):
    a = ans[i]
    if i % 2 == 1:
        a = a[::-1]
    print(' '.join(map(str, a)))
