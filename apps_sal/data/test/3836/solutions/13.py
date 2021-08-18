
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


ans = sum(A[3] or [0])


single = min(len(A[1]), len(A[2]))

ans += sum(A[1][:single] or [0])
ans += sum(A[2][:single] or [0])

x = len(A[3]) + single

a = A[1][single:] + A[2][single:] + A[0]
a.sort(reverse=True)
ans += sum(a[: len(A[3])] or [0])

print(ans)
