import re
import math
import decimal
import bisect
def read(): return input().strip()
def iread(): return int(input().strip())
def viread(): return [int(_) for _ in input().strip().split()]


n = iread()
grid = []
for i in range(n):
    grid.append(read())

ans = 0
for i in range(1, n - 1):
    for j in range(1, n - 1):
        if grid[i][j] == "X" and grid[i - 1][j - 1] == "X" and grid[i - 1][j + 1] == "X" and grid[i + 1][j - 1] == "X" and grid[i + 1][j + 1] == "X":
            ans += 1
print(ans)
