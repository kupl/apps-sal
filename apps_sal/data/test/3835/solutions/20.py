import sys 
from collections import defaultdict
from itertools import combinations
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
arr = [list(map(int, input().split())) for i in range(n)]
ans = [0] * n 

for i in range(n-2):
  ans[i] = int(((arr[i][i+1] * arr[i][i+2]) // arr[i+1][i+2]) ** 0.5)

ans[n - 2] = arr[n - 2][0] // ans[0]
ans[n - 1] = arr[n - 1][0] // ans[0]

print(*ans)


