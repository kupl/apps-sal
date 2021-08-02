N, A, B = [int(i) for i in input().split()]
v = [int(i) for i in input().split()]
v.sort()
v.reverse()
cum = [v[0]]


def comb(n, k):
    if k > n:
        return 0
    ans = 1
    for i in range(k):
        ans *= n - i
    for j in range(k):
        ans = ans // (j + 1)
    return ans


for i in range(1, N):
    cum += [cum[i - 1] + v[i]]
print(('{:.10f}'.format(cum[A - 1] / A)))
target = v[A - 1]
n = v.count(target)
fromk = (A - 1) - v.index(target) + 1
if v[0] == target:
    ans = 0
    for i in range(A, min(B, n) + 1):
        ans += comb(n, i)
    print(ans)
else:
    #print((n, fromk))
    ans = comb(n, fromk)
    print(ans)
