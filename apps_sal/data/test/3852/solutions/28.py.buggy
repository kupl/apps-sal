import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

# N <= 50
if A == sorted(A):
    print(0)
    return

min_a = (float("inf"), -1)
max_a = (-float("inf"), -1)
for i in range(N):
    if A[i] < min_a[0]:
        min_a = (A[i], i)
    if A[i] > max_a[0]:
        max_a = (A[i], i)

# 操作履歴
ops = []
# マイナスに寄せる
if abs(min_a[0]) > abs(max_a[0]):
    for i in range(N - 1, -1, -1):
        # 高々2回
        while A[i] > min_a[0]:
            A[i] += min_a[0]
            ops.append((min_a[1] + 1, i + 1))
        min_a = (A[i], i)

else:
    for i in range(N):
        # 高々2回
        while A[i] < max_a[0]:
            A[i] += max_a[0]
            ops.append((max_a[1] + 1, i + 1))
        max_a = (A[i], i)
# print(A)

print(len(ops))
for (x, y) in ops:
    print(x, y)
