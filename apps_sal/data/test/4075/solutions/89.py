import sys
3
input = lambda: sys.stdin.readline().strip()
n, m = [int(x) for x in input().split()]
s = [[int(x) - 1 for x in input().split()][1:] for i in range(m)]
p = [int(x) for x in input().split()]
print(sum(1 for mask in range(1 << n) if all(sum((mask >> bulb) & 1 for bulb in s[i]) % 2 == p[i] for i in range(m))))
