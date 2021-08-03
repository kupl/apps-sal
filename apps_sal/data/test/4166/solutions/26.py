import math
import decimal
def i_input(): return int(input())


def i_map(): return list(map(int, input().split()))


def i_list(): return list(map(int, input().split()))


def i_row(N): return [int(input()) for _ in range(N)]


def i_row_list(N): return [list(map(int, input().split())) for _ in range(N)]


n, m = i_map()
sc = i_row_list(m)
sc.sort()
num = [-1] * n
ans = -2
for s, c in sc:
    if num[s - 1] == -1:
        num[s - 1] = c
    elif num[s - 1] != -1 and num[s - 1] != c:
        ans = -1
        break
if ans != -1:
    if n == 1:
        if num[0] == -1:
            ans = 0
        else:
            ans = num[0]
    else:
        if num[0] == -1:
            num[0] = 1
        ans = 0
        for i in range(n):
            if num[0] == 0:
                ans = -1
                break
            if num[i] == -1:
                num[i] = 0
            ans += num[i] * (10**(n - 1 - i))
print(ans)
