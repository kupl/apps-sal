n = int(input())
l = list(map(int, input().split()))
l.sort(reverse=1)
res = 0
for i in range(2 * n):
    if i % 2 != 0:
        continue
    res += min(l[i], l[i + 1])
print(res)
