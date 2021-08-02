def Zs(): return list(map(int, input().split()))
def Z(): return int(input())


def solve(n):
    if n <= 3: return None
    ans = []
    k = 1
    while n >= 8:
        ans.extend([k + 1, k + 3, k, k + 2])
        n -= 4
        k += 4
    if n == 4:
        ans.extend([x + k for x in [2, 0, 3, 1]])
    elif n == 5:
        ans.extend([x + k for x in [2, 0, 4, 1, 3]])
    elif n == 6:
        ans.extend([x + k for x in [2, 0, 4, 1, 3, 5]])
    else:
        ans.extend([x + k for x in [2, 0, 4, 1, 5, 3, 6]])
    return ans


for _ in range(Z()):
    n = Z()
    ans = solve(n)
    if ans is not None:
        print(*ans)
    else:
        print(-1)
