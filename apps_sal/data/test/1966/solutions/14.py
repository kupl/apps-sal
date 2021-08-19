n = int(input().split()[0])
#p=[[[None for i in range(n)]for i in range(n)]for i in range(4)]


def cnt(p):
    # print('Hre:')
    # print(len(p))
    # print(len(p[0]))
    # print(p)
    ans = 0
    for i in range(n):
        for j in range(n):
            s = p[i]
            # print(s[j])
            if (i + j) % 2 == int(s[j]):
                ans += 1
    return ans


ans = []
for i in range(4):
    p = []
    while len(p) < n:
        s = input()
        if len(s) == 0:
            continue
        p.append(s)
    ans.append(cnt(p))
    # s=input()
ans.sort()
print(ans[0] + ans[1] + n * n - ans[2] + n * n - ans[3])
