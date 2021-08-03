n, m = list(map(int, input().split()))
ans = [-1 for _ in range(n)]
for _ in range(m):
    s, c = list(map(int, input().split()))
    s -= 1
    if s > n - 1:
        print((-1))
        break
    if ans[s] == -1:
        ans[s] = c
    elif ans[s] != c:
        print((-1))
        break
else:
    A = 0
    for i, a in enumerate(ans[::-1]):
        if a != -1:
            A += 10 ** i * a
        elif i == n - 1 and n != 1:
            A += 10 ** i
    if len(str(A)) != n:
        print((-1))
    else:
        print(A)
