from collections import Counter
n = int(input())
A = Counter(list(map(int, input().split())))
ans = 0
for (k, v) in list(A.items()):
    if k > v:
        ans += v
    elif k < v:
        ans += v - k
print(ans)
