(n, x) = map(int, input().split())
s = sum(map(int, input().split()))
print((abs(s) + x - 1) // x)
