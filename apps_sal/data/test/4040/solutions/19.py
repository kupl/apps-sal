'''
https://codeforces.com/contest/1256/problem/C
'''


n, m, d = list(map(int, input().split()))
cs = list(map(int, input().split()))


ls = [0] * m
ls[m - 1] = cs[m - 1]
for i in range(m - 1):
    ls[m - i - 2] = ls[m - i - 1] + cs[m - i - 2]


if ls[0] + (d - 1) * (m + 1) < n:
    print('NO')
else:
    ns = [0] * n
    ci = 0
    jump = 1
    i = 0
    while i < n and ci < m:
        # print(i)
        # print(n - i)
        if ls[ci] < n - i:
            if jump < d:
                jump += 1
                ns[i] = 0
            else:
                for i in range(i, i + cs[ci]):
                    ns[i] = ci + 1
                    jump = 1
                ci += 1
        else:
            # print(list(range(i, i + cs[ci])))
            for i in range(i, i + cs[ci]):
                ns[i] = ci + 1
                jump = 1
            ci += 1
        i += 1
    print('YES')
    print(' '.join(list(map(str, ns))))

