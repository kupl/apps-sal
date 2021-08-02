import numpy as np

N, A, B = map(int, input().split())

H = []

for i in range(N):
    H.append(int(input()))

H = np.array(H)


def binary_search(x):
    H_tmp = H - B * x
    H_tmp = H_tmp[H_tmp > 0]
    count = ((H_tmp + A - B - 1) // (A - B)).sum()
    return x >= count


left = 0
right = 10**10

while(right - left > 1):
    mid = (left + right) // 2
    ret = binary_search(mid)
    if ret:
        right = mid
    else:
        left = mid

print(right)
