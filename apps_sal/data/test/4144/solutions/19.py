N, = map(int, input().split())
re = 0
re = 10 ** N - ((2 * 9 ** N) - 8 ** N)
print(re%(10**9+7))
