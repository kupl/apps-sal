(N, M, Q) = map(int, input().split())
a = [0] * Q
b = [0] * Q
c = [0] * Q
d = [0] * Q
for i in range(Q):
    (a[i], b[i], c[i], d[i]) = map(int, input().split())


def dfs(n_list, o, l, L):
    if o + l == 0:
        num = 1
        pos = 0
        L_child = [0] * N
        for i in range(N + M - 1):
            if n_list[i] == 1:
                num += 1
            else:
                L_child[pos] = num
                pos += 1
        L.append(L_child)
    if o >= 1:
        n_list[N + M - o - l - 1] = 0
        dfs(n_list, o - 1, l, L)
    if l >= 1:
        n_list[N + M - o - l - 1] = 1
        dfs(n_list, o, l - 1, L)


A = [0] * (N + M - 1)
L = []
dfs(A, N, M - 1, L)
ans = 0
for i in L:
    score = 0
    for j in range(Q):
        if i[b[j] - 1] - i[a[j] - 1] == c[j]:
            score += d[j]
    if score > ans:
        ans = score
print(ans)
