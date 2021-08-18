a = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]


def cal(x):
    y = str(x)
    ans = 0
    for i in y:
        ans = ans + a[int(i)]
    return ans


tt = [0]
for i in range(1, 1000000 + 1):
    tt.append(int(cal(i)))
ss = [0]
for i in range(1, 1000000 + 1):
    ss.append(ss[i - 1] + tt[i])
L, R = list(map(int, input().split()))
print(ss[R] - ss[L - 1])
