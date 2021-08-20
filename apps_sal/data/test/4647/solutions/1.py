import sys
_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__


def go():
    n = int(input())
    a = list(map(int, input().split()))
    e = {i: set() for i in range(n)}
    for _ in range(n - 1):
        (u, v) = list(map(int, input().split()))
        (u, v) = (u - 1, v - 1)
        e[u].add(v)
        e[v].add(u)
    ranks = [len(e[i]) for i in range(n)]
    leafs = [i for i in range(n) if ranks[i] == 1]
    index = 0
    vs = {i: {} for i in range(n)}
    done = set()
    while index < len(leafs):
        cur = leafs[index]
        mysum = sum(vs[cur].values())
        if a[cur] == 0:
            mysum -= 1
        else:
            mysum += 1
        for i in e[cur] - done:
            vs[i][cur] = max(mysum, 0)
            ranks[i] -= 1
            if ranks[i] == 1:
                leafs.append(i)
        done.add(cur)
        index += 1
    sums = [0] * n
    que = [ranks.index(0)]
    done = set()
    index = 0
    while index < len(que):
        cur = que[index]
        mysum = sum(vs[cur].values())
        if a[cur] == 0:
            mysum -= 1
        else:
            mysum += 1
        sums[cur] = mysum
        for i in e[cur] - done:
            vs[i][cur] = max(mysum - vs[cur][i], 0)
            que.append(i)
        done.add(cur)
        index += 1
    return ' '.join(map(str, sums))


for _ in range(1):
    print(go())
