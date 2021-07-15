for _ in range(int(input())):

    n = int(input())
    p = [int(x) - 1 for x in input().split()]

    used = [False] * n
    r = [0] * n

    for i in range(n):
        if not used[i]:
            j = i
            cycle = []
            while not used[j]:
                cycle.append(p[j])
                used[j] = True
                j = p[j]
            for c in cycle:
                r[c] = len(cycle)
    print(*r)

