"""
|    author: mr.math - Hakimov Rahimjon     |
|    e-mail: mr.math0777@gmail.com          |
|    created: 04.02.2018 13:29              |
"""
TN = 1


def solution():
    import re
    (n, m, k) = list(map(int, input().split()))
    s = [input() for _ in range(n)]
    if n > 1 and k > 1:
        t = list([''.join(x) for x in zip(*s)])
        s += t
    ans = 0
    p = re.compile('\\.{' + str(k) + ',}')
    for i in s:
        ans += sum([len(x) - k + 1 for x in p.findall(i)])
    print(ans)


while TN != 0:
    solution()
    TN -= 1
