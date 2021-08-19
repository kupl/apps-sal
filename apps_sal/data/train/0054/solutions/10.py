import collections


def solve():
    n = int(input())
    a = list(map(int, input().split()))
    d = collections.defaultdict(int)
    for i in a:
        d[i] += 1
    for i in range(11):
        d[2 ** (i + 1)] += d[2 ** i] // 2
    if d[2 ** 11]:
        print('YES')
    else:
        print('NO')


t = int(input())
for _ in range(t):
    solve()
