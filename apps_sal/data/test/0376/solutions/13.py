def main():
    n = int(input())
    a = list(map(int, input().split()))
    graph = [[] for _ in range(n)]
    for i in range(n - 1):
        u, v = [int(x) - 1 for x in input().split()]
        graph[u].append(v)
        graph[v].append(u)

    a_max = max(a)
    max_count_0 = sum(ai == a_max for ai in a)
    prev_count_0 = sum(ai == a_max - 1 for ai in a)

    result = a_max + 2
    for u in range(n):
        max_count = max_count_0
        prev_count = prev_count_0
        if a[u] == a_max:
            max_count -= 1
        else:
            prev_count -= 1

        for v in graph[u]:
            if a[v] == a_max:
                max_count -= 1
                prev_count += 1
            elif a[v] == a_max - 1:
                prev_count -= 1

        if max_count == 0:
            if prev_count == 0:
                result = a_max
                break
            else:
                result = a_max + 1

    print(result)


def __starting_point():
    main()


__starting_point()
