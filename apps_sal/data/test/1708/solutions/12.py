from collections import deque
import sys
stdin = sys.stdin

sys.setrecursionlimit(10**5)


def li(): return map(int, stdin.readline().split())
def li_(): return map(lambda x: int(x) - 1, stdin.readline().split())
def lf(): return map(float, stdin.readline().split())
def ls(): return stdin.readline().split()
def ns(): return stdin.readline().rstrip()
def lc(): return list(ns())
def ni(): return int(stdin.readline())
def nf(): return float(stdin.readline())


n, m = li()
a = list(li())
c = list(li())

# dictionary of idx-num
dic = {idx: ai for idx, ai in enumerate(a)}

# cheap order
cord = [idx for (_, idx) in sorted([(ci, idx) for idx, ci in enumerate(c)])]
cord = deque(cord)

for _ in range(m):
    dish, num = li()
    dish -= 1

    ans = 0

    if num <= dic[dish]:
        dic[dish] -= num
        ans = c[dish] * num
        print(ans)

    else:
        ans = c[dish] * dic[dish]
        num -= dic[dish]
        dic[dish] = 0

        while num > 0:
            if cord:
                nex = cord.popleft()
            else:
                ans = 0
                num = 0

            if dic[nex] > num:
                ans += c[nex] * num
                dic[nex] -= num
                cord.appendleft(nex)
                num = 0

            elif dic[nex] == num:
                ans += c[nex] * num
                dic[nex] = 0
                num = 0

            else:
                ans += c[nex] * dic[nex]
                num -= dic[nex]
                dic[nex] = 0

        print(ans)
