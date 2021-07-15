ii = lambda: int(input())
mi = lambda: map(int, input().split())
li = lambda: list(mi())

n, m, k = mi()
print('Yes' if min(m, k) >= n else 'No')
