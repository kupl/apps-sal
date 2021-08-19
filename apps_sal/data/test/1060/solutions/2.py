def clique_in_the_divisibility_graph(n, a):
    MAX = 10 ** 6 + 1
    L = [0] * MAX
    for v in a:
        L[v] = 1
    for i in range(n):
        if L[a[i]]:
            for x in range(a[i] * 2, MAX, a[i]):
                if L[x]:
                    L[x] = max(L[x], L[a[i]] + 1)
    return max(L)


def __starting_point():
    n = int(input())
    a = list(map(int, input().split()))
    result = clique_in_the_divisibility_graph(n, a)
    print(result)


__starting_point()
