
import sys

n = int(input())
t, a = list(map(int, input().split()))

h = list(map(int, input().split()))

ls = [abs(a - (t - (h[i] * 0.006))) for i in range(n)]

m = min(ls)

ans = ls.index(m) + 1

print(ans)
