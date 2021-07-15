import sys

H, W = map(int, sys.stdin.readline().split())
print("#" * (W + 2))
for _ in range(H):
    s = sys.stdin.readline().strip()
    print("#" + s + "#")
print("#" * (W + 2))
