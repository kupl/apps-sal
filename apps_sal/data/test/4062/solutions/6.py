from sys import stdin
(a, b, c, d) = [int(_) for _ in stdin.readline().rstrip().split()]
print(max([a * c, a * d, b * c, b * d]))
