(n, s) = map(int, input().split())
a = sorted(map(int, input().split()))
print('NO' if sum(a[:n - 1]) > s else 'YES')
