from sys import stdin
n, m = map(int, stdin.readline().split() )
print(max(n,m) - 1, min(n,m))
