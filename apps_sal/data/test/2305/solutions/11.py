import sys
sys.setrecursionlimit(10**6)


def main():
    n = int(input())
    color = list(map(int, input().split()))
    nodes = [[]for i in range(n)]
    cut = [[0]for i in range(n + 1)]
    ans = [0] * (n + 1)
    for i in range(n - 1):
        a, b = map(int, input().split())
        nodes[a - 1].append(b - 1)
        nodes[b - 1].append(a - 1)

    def num(p, parent):
        s = 0
        for child in nodes[p]:
            if child == parent:
                continue
            cut[color[p]].append(0)
            nc = num(child, p)
            group = nc - cut[color[p]].pop()
            ans[color[p]] += group * (group + 1) // 2
            s += nc
        s += 1
        cut[color[p]][-1] += s
        return s
    num(0, -1)
    for a, c in zip(ans[1:], cut[1:]):
        group = n - c[0]
        c = group * (group + 1) // 2
        print(n * (n + 1) // 2 - c - a)


main()
