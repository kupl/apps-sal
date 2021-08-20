from collections import Counter
n = int(input())
a = list(map(int, input().split()))
a = Counter(a)
lis = []
for (i, j) in a.items():
    lis += [i] * (j // 2)
lis.sort(reverse=True)
if len(lis) <= 1:
    ans = 0
else:
    ans = lis[0] * lis[1]
print(ans)
