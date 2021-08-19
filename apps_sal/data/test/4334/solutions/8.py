(s, t) = input().split()
(a, b) = map(int, input().split())
n = [(a, b - 1), (a - 1, b)][s == input()]
print(*n, sep=' ')
