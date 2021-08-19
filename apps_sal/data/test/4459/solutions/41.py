import collections
N = int(input())
a = list(map(int, input().split()))
A = collections.Counter(a)
ans = 0
for (i, j) in A.items():
    if j > i:
        ans += j - i
    elif i > j:
        ans += j
print(ans)
