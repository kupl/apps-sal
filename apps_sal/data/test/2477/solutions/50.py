from math import ceil


def check(x):
    # 全てを長さx以下にするために必要な回数
    cnt = 0
    for a in A:
        # 切る回数は-1した回数。a=20 x=4 20/4=5 だが切る箇所は4。
        cnt += ceil(a / x) - 1
    return cnt <= K


N, K = list(map(int, input().split()))
A = list(map(int, input().split()))

left = 0
right = max(A)
while left < right - 1:
    mid = (left + right) // 2
    if check(mid):
        right = mid
    else:
        left = mid
print(right)
