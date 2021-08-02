from collections import deque
import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readlines


def main():

    lines = input()
    n, k = list(map(int, lines[0].split()))
    a = [[] for i in range(n + 1)]

    for i in range(1, n):
        r, l = list(map(int, lines[i].split()))
        a[r].append(l)
        a[l].append(r)

    que = deque()
    que.append(1)
    colors = [-1] * (n + 1)
    colors[1] = k
    ways = k

    while que:
        p = que.popleft()
        # root no toki
        if p == 1:
            now_color = k
            for son in a[p]:
                now_color -= 1
                ways = (ways * now_color) % 1_000_000_007
                colors[son] = now_color
                que.append(son)
        else:
            now_color = k - 1
            for son in a[p]:
                if colors[son] < 0:
                    now_color -= 1
                    colors[son] = now_color
                    ways = (ways * now_color) % 1_000_000_007
                    que.append(son)

    print(ways)


main()
