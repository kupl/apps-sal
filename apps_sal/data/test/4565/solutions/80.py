from itertools import accumulate
n = int(input())
s = list(input())
l = [1 if s[i] == 'E' else 0 for i in range(n)]
l = list(accumulate(l))
ans = l[-1] - l[0]
for i in range(1, n):
    ans = min(ans, i - l[i - 1] + l[-1] - l[i])
print(ans)
