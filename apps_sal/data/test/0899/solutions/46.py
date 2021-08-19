def main():
    from sys import stdin

    def input():
        return stdin.readline().strip()

    n, m = map(int, input().split())
    tree = [[] for _ in range(n)]
    for _ in range(m):
        i, j, k = map(int, input().split())
        i -= 1
        j -= 1
        tree[i].append((k, j))
        tree[j].append((k, i))

    # dijkstra
    import heapq
    from numpy import zeros

    ans = 0
    for i in range(n):
        for j in tree[i]:
            seen = zeros(n)
            goal = j[1]
            base = j[0]
            seen[i] = 1
            todo = []
            heapq.heapify(todo)
            for k in tree[i]:
                if k[0] < base and k != j:
                    heapq.heappush(todo, k)
            while len(todo) > 0:
                k = heapq.heappop(todo)
                if k[1] == goal:
                    if k[0] < base:
                        ans += 1
                    break
                seen[k[1]] = 1
                for l in tree[k[1]]:
                    if seen[l[1]] == 0 and k[0] + l[0] < base:
                        heapq.heappush(todo, (k[0] + l[0], l[1]))

    print(ans // 2)


main()
