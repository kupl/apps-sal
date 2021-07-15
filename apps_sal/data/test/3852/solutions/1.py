# coding:UTF-8
import sys

MOD = 10 ** 9 + 7
INF = float('inf')

N = int(input())    # 数字
a = list(map(int, input().split()))     # スペース区切り連続数字
a_res = [0] * N

m_value = 0
m_pos = -1

for i in range(N):
    if abs(a[i]) > abs(m_value):
        m_value = a[i]
        m_pos = i

res = []
if m_pos == -1:
    print(0)
    return

if m_value > 0:
    v = a[0]
    for i in range(N):
        if a[i] >= v:
            v = a[i]
            a_res[i] = a[i]
        else:
            a_tmp = a[i]
            a_tmp += m_value
            res.append([m_pos, i])
            if a_tmp < v:
                a_tmp += m_value
                res.append([m_pos, i])
            a_res[i] = a_tmp
            v = a_tmp
            if a_tmp > m_value:
                m_value = a_tmp
                m_pos = i
else:
    v = a[-1]
    for i in reversed(range(N)):
        if a[i] <= v:
            v = a[i]
            a_res[i] = a[i]
        else:
            a_tmp = a[i]
            a_tmp += m_value
            res.append([m_pos, i])
            if a_tmp > v:
                a_tmp += m_value
                res.append([m_pos, i])
            a_res[i] = a_tmp
            v = a_tmp
            if a_tmp < m_value:
                m_value = a_tmp
                m_pos = i


print("{}".format(len(res)))
for i in range(len(res)):
    print("{} {}".format(res[i][0]+1, res[i][1]+1))
