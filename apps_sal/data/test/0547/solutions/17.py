
n, k = [int(x) for x in input().split()]
passes = [input() for _ in range(n)]
password = input()

l = len([p for p in passes if len(p) < len(password)]) + 1
h = len([p for p in passes if len(p) <= len(password)])

l += ((l - 1) // k) * 5
h += ((h - 1) // k) * 5

print(l, h)
