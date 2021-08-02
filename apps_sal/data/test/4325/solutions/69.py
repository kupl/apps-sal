#d,t,s = list(map(int, input().split()))
n, x, t = list(map(int, input().split()))

print(((n + x - 1) // x * t))
