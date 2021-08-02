H, N = map(int, input().split())
A = []
B = []
for i in range(N):
    n, a = input().split()
    A.append(int(n))
    B.append(int(a))


def f(x):
    if x <= 0:
        return 0
    else:
        mini = g(x - A[0]) + B[0]
        for i in range(1, N):
            sub = g(x - A[i]) + B[i]
            if sub < mini:
                mini = sub
        return mini


def g(x):
    if x < 0:
        return 0
    else:
        return g_list[x]


g_list = []
g_list.append(0)
for i in range(1, H + 1):
    g_list.append(f(i))
print(g_list[-1])
