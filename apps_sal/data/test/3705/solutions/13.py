import sys

n = int(sys.stdin.readline())
s = input()

x = s.count("8")

print(min(n // 11, x))
