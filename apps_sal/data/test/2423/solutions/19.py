"""
|    author: mr.math - Hakimov Rahimjon     |
|    e-mail: mr.math0777@gmail.com          |
|    created: 14.04.2018 16:50              |
"""
TN = 1


def solution():
    n = int(input())
    l = [[0 for j in range(n)] for i in range(n)]
    ans = 0
    for i in range(n - 1):
        (u, v) = list(map(int, input().split()))
        l[u - 1][v - 1] = 1
        l[v - 1][u - 1] = 1
    for i in l:
        if i.count(1) == 1:
            ans += 1
    print(ans)


while TN != 0:
    solution()
    TN -= 1
