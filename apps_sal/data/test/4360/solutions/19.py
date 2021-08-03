from sys import stdin

n = int(stdin.readline().rstrip())
A = [int(a) for a in stdin.readline().rstrip().split()]

A = [float(a) for a in A]

total = 0.

for a in A:
    total += 1 / a

print(1 / total)
