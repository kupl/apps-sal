# D - Lunlun Number
import sys
sys.setrecursionlimit(10**6 + 1)
K = int(input())

ans = []


def dfs(A):
    if len(A) >= 2:
        A_str = [str(i) for i in A]
        A_str = ''.join(A_str)
        ans.append(int(A_str))
    if len(A) == 10:
        return
    if len(A) >= 1:
        # 前の値が0,9のときは範囲が違う
        if A[-1] == 9:
            sta = 8
            fin = 9 + 1
        elif A[-1] == 0:
            sta = 0
            fin = 1 + 1
        else:
            sta = A[-1] - 1
            fin = A[-1] + 1 + 1
        for v in range(sta, fin):
            A.append(v)
            dfs(A)
            A.pop()
    else:
        for v in range(1, 9 + 1):
            A.append(v)
            dfs(A)
            A.pop()


dfs([])
ans = sorted(ans, reverse=False)
if K <= 9:
    print(K)
else:
    print(ans[K - 10])
