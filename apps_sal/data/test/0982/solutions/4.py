for _ in range(int(input())):
    l, r = map(int, input().split())
    print(["NO", "YES"][r < 2 * l])
