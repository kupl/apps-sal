from collections import deque
from sys import stdin, stdout
input = stdin.readline
print = stdout.write

anss = []
t = int(input())

for test_count in range(t):
    ans = 1
    part = 0
    factor = 0
    queue = deque([])
    n, m = map(int, input().split())
    if m > (n // 2) * (n // 2 + 1):
        anss.append(0)
        for edge_count in range(m):
            input()
        continue
    edge = [[] for i in range(n + 1)]
    flag = [-1] * (n + 1)
    assure = 1

    for edge_count in range(m):
        u, v = map(int, input().split())
        edge[u].append(v)
        edge[v].append(u)
    flag[1] = 0
    queue.append(1)

    break_all = False
    while not break_all:
        even, odd = 1, 0
        while queue and not break_all:
            search = queue.popleft()
            # print('searching vertex {0}, {1}'.format(search, edge[search]))
            current = flag[search]
            for to in edge[search]:
                if flag[to] == -1:
                    flag[to] = current ^ 1
                    if flag[to] & 1:
                        odd += 1
                    else:
                        even += 1
                    queue.append(to)
                elif flag[to] == current:
                    break_all = True
                else:
                    assert flag[to] == current ^ 1
        # print(flag)
        if break_all:
            # print('break_all')
            ans = 0
        else:
            if (even, odd) == (1, 0):
                factor += 1
            else:
                ans *= pow(2, even, 998244353) + pow(2, odd, 998244353)
                ans %= 998244353
        while assure <= n:
            if flag[assure] == -1:
                part += 1
                flag[assure] = 2 * part

                queue.append(assure)
                break
            assure += 1
        if assure == n + 1:
            break
    ans *= pow(3, factor, 998244353)
    ans %= 998244353
    anss.append(ans)
print('\n'.join(map(str, anss)))
# print(time.time() - start)
