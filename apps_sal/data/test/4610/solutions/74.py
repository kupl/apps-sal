from collections import Counter

n, k = list(map(int, input().split()))
a = Counter(list(map(int, input().split())))
a = list(a.items())
a.sort(key=lambda x: x[1])
opt = len(a) - k
ans = 0
if opt > 0:
    for i in range(opt):
        ans += a[i][1]
print(ans)
