import math
import decimal
def i_input(): return int(input())


def i_map(): return map(int, input().split())


def i_list(): return list(map(int, input().split()))


def i_row(N): return [int(input()) for _ in range(N)]


def i_row_list(N): return [list(map(int, input().split())) for _ in range(N)]


n = i_input()
aa = i_list()
aa.sort()
ans = 1
for a in aa:
    ans *= a
    if ans > 10**18:
        ans = -1
        break
print(ans)
