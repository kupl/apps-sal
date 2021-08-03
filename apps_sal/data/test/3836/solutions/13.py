# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 11/3/18

"""


N = int(input())

A = [[] for _ in range(4)]
a, b, c, d = A
for ni in range(N):
    v, f = input().split()
    A[int(v, 2)].append(int(f))


for i in range(len(A)):
    A[i].sort(reverse=True)


# all people '11' supports both will be selected
ans = sum(A[3] or [0])

# select equal number of '01' or '10'

single = min(len(A[1]), len(A[2]))

ans += sum(A[1][:single] or [0])
ans += sum(A[2][:single] or [0])

x = len(A[3]) + single
# select left '01' '10' or '00' make total people <= 2*x, current have 2*single + len(A[3])
# so at most select len(A[3]) more people

a = A[1][single:] + A[2][single:] + A[0]
a.sort(reverse=True)
ans += sum(a[: len(A[3])] or [0])

print(ans)
