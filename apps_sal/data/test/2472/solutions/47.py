def main():
    N = int(input())
    works = []
    for i in range(N):
        A, B = list(map(int, input().split()))
        works.append((A, B))

    works.sort(key=lambda x: x[1])

    time = 0
    for i in range(N):
        a, b = works[i]
        time += a
        if time > b:
            print('No')
            return
    print('Yes')


def __starting_point():
    main()


__starting_point()
