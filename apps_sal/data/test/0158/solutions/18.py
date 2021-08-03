n = int(input())
l = sorted(map(int, input().split()))

print(['NO', 'YES'][l[n] > l[n - 1]])
