import numpy as np
import sys
input = sys.stdin.readline

# 奇数番目、または偶数番目、の好きな部分集合を足せる（ただし1元以上）
# 交互に塗り分けると交互が維持されることから分かる

N = int(input())
A = np.array(input().split(), dtype=np.int64)


def select_operation(select, N):
    result = []
    # 余分な左端
    x = select.min()
    result = [0] * x
    select -= x
    N -= x
    # 余分な右端
    y = select.max()
    result += list(range(N - 1, y, -1))
    N = y + 1
    # 右から見て、要らない偶数を除外
    result += np.setdiff1d(np.arange(N)[::2], select)[::-1].tolist()
    # 0,2,4,...番目を集約
    result += [1] * (len(select) - 1)
    result = [1 + x for x in result]
    return result


ev_sum = np.maximum(0, A[::2]).sum()
od_sum = np.maximum(0, A[1::2]).sum()
if ev_sum >= od_sum > 0:
    select = np.where(A[::2] >= 0)[0] * 2
elif od_sum > 0:
    select = np.where(A[1::2] >= 0)[0] * 2 + 1
else:
    n = np.argmax(A)
    select = np.array([n])
S = A[select].sum()

ope = select_operation(select, N)

# 答えの出力
print(S)
print(len(ope))
print('\n'.join(map(str, ope)))

select
