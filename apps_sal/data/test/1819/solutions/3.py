ii = lambda: int(input())
mi = lambda: list(map(int, input().split()))
li = lambda: list(mi())

for _ in range(ii()):
    x, n = mi()
    print(n * 2)

