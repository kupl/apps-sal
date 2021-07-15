import sys
input = sys.stdin.readline
A, B = map(int, input().split())
a = [["#"] * 100 for _ in range(100)]
for i in range(100):
  a[i][0] = "."
for i in range(0, 100, 2):
  for j in range(1, 99):
    a[i][j] = "."
for i in range(0, 100, 2):
  for j in range(1, 99, 2):
    if A <= 1: break
    A -= 1
    a[i][j] = "#"
for i in range(99, -1, -2):
  for j in range(98, 0, -2):
    if B <= 1: break
    B -= 1
    a[i][j] = "."
print(100, 100)
for r in a: print("".join(r))
