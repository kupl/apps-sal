from bisect import bisect_left
n = int(input())
a = list(map(int, input().split()))
bl = [0]
for i in a:
    bl.append(bl[-1] + i)
br = [0]
for i in a[::-1]:
    br.append(br[-1] + i)


def fl(r):
    suma = bl[r + 1]
    ir = bisect_left(bl, suma // 2)
    (ans11, ans12) = (bl[ir], suma - bl[ir])
    (ans21, ans22) = (bl[ir - 1], suma - bl[ir - 1])
    if abs(ans11 - ans12) < abs(ans21 - ans22):
        return [ans11, ans12]
    else:
        return [ans21, ans22]


def fr(l):
    r = n - 1 - l
    suma = br[r + 1]
    ir = bisect_left(br, suma // 2)
    (ans11, ans12) = (br[ir], suma - br[ir])
    (ans21, ans22) = (br[ir - 1], suma - br[ir - 1])
    if abs(ans11 - ans12) < abs(ans21 - ans22):
        return [ans11, ans12]
    else:
        return [ans21, ans22]


ans = 10 ** 20
for i in range(1, n - 1):
    l = i
    r = i + 1
    (ll, lr) = fl(i)
    (rl, rr) = fr(i + 1)
    ans = min(ans, max(ll, lr, rl, rr) - min(ll, lr, rl, rr))
print(ans)
