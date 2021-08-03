def R(): return map(int, input().split())


n, a, b = R()


def T(): return list(map(int, input().split()))


A = T()
B = T()
ans = [-1 for i in range(n + 1)]
for i in range(a):
    ans[A[i]] = 1
for i in range(1, n + 1):
    if ans[i] == -1:
        ans[i] = 2
for i in range(1, n + 1):
    print(ans[i], end=' ')
