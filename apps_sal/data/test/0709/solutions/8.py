import sys
lines = sys.stdin.read().split('\n')
n = int(lines[0])
print(sum(map(int, bin(n)[2:])))
