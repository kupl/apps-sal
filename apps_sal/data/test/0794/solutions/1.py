
def __starting_point():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    if sum(a[:n]) == sum(a[n:]):
        print(-1)
    else:
        print(' '.join(map(str, a)))


__starting_point()
