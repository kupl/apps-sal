from collections import Counter
n = int(input())
a = list(map(int, input().split()))
num = Counter(a)

if n == len(num) + 1 or n == len(num):
    print((0))
    return

ans = []

for i in num:
    if num[i] >= 2:
        ans.append(i)
    if num[i] >= 4:
        ans.append(i)
n = max(ans)
ans.pop(ans.index(max(ans)))
m = max(ans)
print((n * m))
