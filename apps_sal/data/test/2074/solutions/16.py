def main():
    n, m = map(int, input().split())
    l = []

    for _ in range(n):
        a = list(map(int, input().split()))
        l.append(min(a))

    print(max(l))

def __starting_point():
    main()
__starting_point()
