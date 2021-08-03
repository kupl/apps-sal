def ii(): return int(input())
def mi(): return list(map(int, input().split()))
def li(): return list(mi())


for _ in range(ii()):
    x, n = mi()
    print(n * 2)
