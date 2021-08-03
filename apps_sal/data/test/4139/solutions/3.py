#C - 755
import sys
sys.setrecursionlimit(10**6)
N = input()

lis = ['3', '5', '7']
count = 0


def dfs(A):
    nonlocal lis
    nonlocal count
    if len(A) >= len(N):
        A_str = ''.join(A)
        A_int = int(A_str)
        N_int = int(N)
        if N_int < A_int:
            return
    if len(set(A)) == 3:
        count += 1
    for v in range(3):
        A.append(lis[v])
        dfs(A)
        A.pop()


dfs([])
print(count)
