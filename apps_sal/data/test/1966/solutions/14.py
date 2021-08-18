n = int(input().split()[0])


def cnt(p):
    ans = 0
    for i in range(n):
        for j in range(n):
            s = p[i]
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
ans.sort()
print(ans[0] + ans[1] + n * n - ans[2] + n * n - ans[3])
