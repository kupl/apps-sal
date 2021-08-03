from collections import deque


def solve(s, l, r, k):
    s1, s2 = s[:l - 1], s[r:]
    tmp = s[l - 1: r]
    k %= (r - l + 1)
    d = deque(tmp)
    for _ in range(k):
        x = d[-1]
        d.pop()
        d.appendleft(x)
    tmp = ''.join(d)
    return ''.join([s1, tmp, s2])


s = input()

m = int(input())

for _ in range(m):
    l, r, k = list(map(int, input().split()))
    s = solve(s, l, r, k)

print(s)
