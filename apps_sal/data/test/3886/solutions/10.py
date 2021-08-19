s0 = 'What are you doing at the end of the world? Are you busy? Will you save us?'
s1 = 'What are you doing while sending "'
s2 = '"? Are you busy? Will you send "'
l0 = len(s0)
l1 = len(s1)
l2 = len(s2)


def get(h):
    if h > 55:
        return 10 ** 20
    return (l0 + l1 + l2 + 2 << h) - l1 - l2 - 2


def solve(n, k):
    if get(n) <= k:
        return '.'
    while True:
        if n == 0:
            return s0[k]
        if k < l1:
            return s1[k]
        k -= l1
        if k < get(n - 1):
            n -= 1
            continue
        k -= get(n - 1)
        if k < l2:
            return s2[k]
        k -= l2
        if k < get(n - 1):
            n -= 1
        else:
            return '"?'[k - get(n - 1)]


q = int(input())
for i in range(q):
    (n, k) = list(map(int, input().split()))
    print(solve(n, k - 1), end='')
