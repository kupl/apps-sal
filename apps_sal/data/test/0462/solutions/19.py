from sys import stdin as fin

a, b, c = sorted(map(int, fin.readline().split()))
print(c - a)
