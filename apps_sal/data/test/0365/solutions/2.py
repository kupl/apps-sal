(n, x) = map(int, input().split())
print(['NO', 'YES'][sum(map(int, input().split())) + n - 1 == x])
