import sys

lines = sys.stdin.read().split("\n")
# n, k = map(int, lines[0].split(" "))
# n = int(lines[0])
# nums = list(map(int, lines[1].split(" ")))

n = int(lines[0])
print(sum(map(int, bin(n)[2:])))

