import sys


def inputr():
    return sys.stdin.readline().rstrip('\n')


input = sys.stdin.readline
for _ in range(int(input())):
    (n, m) = list(map(int, input().split()))
    adj = [[] for _ in range(n)]
    for _ in range(m):
        (a, b) = list(map(int, input().split()))
        a -= 1
        b -= 1
        adj[a].append(b)
    LP = [0] * n
    r = []
    for i in range(n):
        if LP[i] < 2:
            for j in adj[i]:
                LP[j] = max(LP[j], LP[i] + 1)
        else:
            r.append(str(i + 1))
    print(len(r))
    print(*r)
    assert 7 * len(r) <= 4 * n
