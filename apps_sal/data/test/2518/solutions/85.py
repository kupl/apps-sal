import numpy as np

N, A, B = list(map(int, input().split()))
H = np.zeros(shape=N, dtype='int64')
for _ in range(N):
    h = int(input())
    H[_] = h


def calc(num, a):
    a -= num * B
    a = (a - 1) // (A - B) + 1
    if sum(a[a > 0]) <= num:
        return True
    else:
        return False


start = 0
end = 10 ** 10

while end - start > 1:
    mid = (start + end) // 2
    if calc(mid, H.copy()):
        end = mid
    else:
        start = mid

print(end)
