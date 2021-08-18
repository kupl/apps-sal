import sys
k = int(input())
lst = [[0] * 10 for i in range(10)]
for i in range(10):
    lst[0][i] = 1
l_sum = [9]


for i in range(1, 10):
    s = 0
    for j in range(10):
        if j == 0:
            lst[i][j] = lst[i - 1][j] + lst[i - 1][j + 1]
        elif j == 9:
            lst[i][j] = lst[i - 1][j] + lst[i - 1][j - 1]
        else:
            lst[i][j] = lst[i - 1][j - 1] + lst[i - 1][j] + lst[i - 1][j + 1]

        if j != 0:
            s += lst[i][j]
    l_sum.append(s + l_sum[-1])


# 表を逆から辿っていく、さらに手直し
i = 0
if k < l_sum[0]:
    print(k)
    return
else:
    while True:
        if k < l_sum[i]:
            break
        i += 1
    k = k - l_sum[i - 1]

    ans = []
    for j in reversed(list(range(0, i + 1))):

        if j == i:
            p = 1
            while True:
                if k - lst[j][p] <= 0:
                    ans.append(p)
                    break
                else:
                    k -= lst[j][p]
                    p += 1

        else:
            if p == 0:
                if k <= lst[j][p]:
                    ans.append(p)
                else:
                    k -= lst[j][p]
                    p += 1
                    ans.append(p)

            elif p == 9:
                if k <= lst[j][p - 1]:
                    p = p - 1
                    ans.append(p)
                else:
                    k -= lst[j][p - 1]
                    ans.append(p)

            else:
                if k <= lst[j][p - 1]:
                    p = p - 1
                    ans.append(p)
                else:
                    k -= lst[j][p - 1]
                    if k <= lst[j][p]:
                        ans.append(p)
                    else:
                        k -= lst[j][p]
                        p = p + 1
                        ans.append(p)

l_s = [str(q) for q in ans]
print((''.join(l_s)))
