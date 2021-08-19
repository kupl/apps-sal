import sys

sys.setrecursionlimit(10 ** 9)
N = input()
N_len = len(N)
'''
75333
'''


# t = []


def dfs(a, depth):
    if depth == N_len:
        if int(a) <= int(N) and a.count('3') > 0 \
                and a.count('5') > 0 and a.count('7') > 0 and str(int(a)).count('0') == 0:
            return 1
        else:
            return 0

    ret1 = dfs(a + '0', depth + 1)
    ret2 = dfs(a + '3', depth + 1)
    ret3 = dfs(a + '5', depth + 1)
    ret4 = dfs(a + '7', depth + 1)
    return ret1 + ret2 + ret3 + ret4


ans = dfs('', 0)
print(ans)
# print(t)
