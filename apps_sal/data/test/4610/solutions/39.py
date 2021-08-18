from collections import Counter
import sys
sys.setrecursionlimit(10**6)


n, k = list(map(int, input().split()))
a = list(map(int, input().split()))

c = Counter(a)

c = list(c.most_common())
len_c = len(c)
ans = 0
while(len_c - k > 0):
    i, j = c.pop()
    len_c -= 1
    ans += j
print(ans)
