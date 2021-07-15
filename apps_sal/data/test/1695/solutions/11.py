import sys 
import itertools
input = lambda: sys.stdin.readline().rstrip()

n, m = list(map(int, input().split()))
arr = [input() for i in range(n)]
score = list(map(int, input().split()))

ans = 0
for i in range(m):
  a = [s[i] for s in arr]
  b = max([a.count(k) for k in "ABCDE"])
  ans += score[i] * b 

print(ans)

