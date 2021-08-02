h, w = map(int, input().split())
ab = []
for i in range(h * 2):
    ab.extend(list(map(int, input().split())))

abs_table = [[0] * w for _ in range(h)]
dp = [[0] * w for _ in range(h)]

s = h * w
i = 0
j = 0
for k in range(s):
    if w == j:
        j = 0
        i += 1
    a, b = ab[k], ab[k + s]
    abs_table[i][j] = abs(a - b)
    j += 1

n = abs_table[0][0]
dp[0][0] = 2**(n * 2) | 1

for i in range(h):
    for j in range(w):
        a = abs_table[i][j]
        u = 0
        l = 0
        if i:
            u = dp[i - 1][j]
            u = u << a * 2 | u | u
        if j:
            l = dp[i][j - 1]
            l = l << a * 2 | l | l

        if not u and not l:
            pass
        elif not l:
            dp[i][j] = u
        elif not u:
            dp[i][j] = l
        else:
            len_u = len(bin(u)[2:])
            len_l = len(bin(l)[2:])
            delta = len_u - len_l
            if delta == 0:
                dp[i][j] = u | l
            elif delta < 0:
                dp[i][j] = u << abs(delta) // 2 | l
            else:
                dp[i][j] = u | l << delta // 2

flag = bin(dp[-1][-1])[2:]
zero = len(flag) // 2
for i, v in enumerate(flag[zero:]):
    if v == '1':
        print(i)
        break
