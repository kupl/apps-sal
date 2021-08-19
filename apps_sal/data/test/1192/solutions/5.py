def f(p):
    ans = 0
    for i in range(len(p)):
        for j in range(i, len(p)):
            if p[i] > p[j]:
                ans += 1
    return ans


(n, k) = list(map(int, input().split()))
p = list(map(int, input().split()))
num = 0
cnt = 0
if k == 1:
    tmp = []
    for i in range(n):
        for j in range(i + 1):
            tmp = p[0:j] + list(reversed(p[j:i + 1])) + p[i + 1:]
            num += 1
            cnt += f(tmp)
elif k == 2:
    tmp1 = []
    tmp2 = []
    for i in range(n):
        for j in range(i + 1):
            tmp1 = p[0:j] + list(reversed(p[j:i + 1])) + p[i + 1:]
            for i1 in range(n):
                for j1 in range(i1 + 1):
                    tmp2 = tmp1[0:j1] + list(reversed(tmp1[j1:i1 + 1])) + tmp1[i1 + 1:]
                    num += 1
                    cnt += f(tmp2)
elif k == 3:
    tmp1 = []
    tmp2 = []
    tmp3 = []
    for i in range(n):
        for j in range(i + 1):
            tmp1 = p[0:j] + list(reversed(p[j:i + 1])) + p[i + 1:]
            for i1 in range(n):
                for j1 in range(i1 + 1):
                    tmp2 = tmp1[0:j1] + list(reversed(tmp1[j1:i1 + 1])) + tmp1[i1 + 1:]
                    for i2 in range(n):
                        for j2 in range(i2 + 1):
                            num += 1
                            tmp3 = tmp2[0:j2] + list(reversed(tmp2[j2:i2 + 1])) + tmp2[i2 + 1:]
                            cnt += f(tmp3)
elif k == 4:
    tmp1 = []
    tmp2 = []
    tmp3 = []
    tmp4 = []
    for i in range(n):
        for j in range(i + 1):
            tmp1 = p[0:j] + list(reversed(p[j:i + 1])) + p[i + 1:]
            for i1 in range(n):
                for j1 in range(i1 + 1):
                    tmp2 = tmp1[0:j1] + list(reversed(tmp1[j1:i1 + 1])) + tmp1[i1 + 1:]
                    for i2 in range(n):
                        for j2 in range(i2 + 1):
                            tmp3 = tmp2[0:j2] + list(reversed(tmp2[j2:i2 + 1])) + tmp2[i2 + 1:]
                            for i3 in range(n):
                                for j3 in range(i3 + 1):
                                    tmp4 = tmp3[0:j3] + list(reversed(tmp3[j3:i3 + 1])) + tmp3[i3 + 1:]
                                    num += 1
                                    cnt += f(tmp4)
print(cnt / num)
