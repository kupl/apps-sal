from sys import stdin as fin
# fin = open("cfr417c.in", "r")

n, S = map(int, fin.readline().split())
arr = list(map(int, fin.readline().split()))


def test(k):
    nonlocal arr, n, S
    costs = sorted([arr[i] + (i + 1) * k for i in range(n)])
    csum = sum(costs[:k])
    # print(costs)
    if csum <= S:
        return csum
    else:
        return 0


l, r, m = 0, n + 1, 0
ans, ansm = 0, 0
while l + 1 != r:
    m = (l + r) // 2
    # print(l, r, m)
    csum = test(m)
    if not csum:
        r = m
    else:
        ans = csum
        ansm = m
        l = m
print(ansm if ans else 0, ans)
