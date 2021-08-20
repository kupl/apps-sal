(N, D) = list(map(int, input().split()))
L = [0] * N
cnt = 0
ans = 0
for i in range(N):
    (x, y) = list(map(int, input().split()))
    L[i] = (x ** 2 + y ** 2) ** 0.5
for i in range(N):
    if L[i] <= D:
        cnt += 1
    else:
        cnt = cnt
ans = cnt
print(ans)
