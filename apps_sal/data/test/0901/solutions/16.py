n, m = map(int, input().split())


def main():
    for i in range(m):
        g = list(map(int, input().split()))
        k = g[0]

        free = set()
        maybe = True
        for j in range(1, k + 1):
            if -g[j] in free:
                maybe = False
                break
            else:
                free.add(g[j])

        if (len(free) > 0) and maybe:
            return "YES"

    return "NO"


print(main())
