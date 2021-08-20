from collections import Counter
md = 10 ** 9 + 7
m = int(input())
cnt = Counter(list(map(int, input().split())))
ans = x = 1
for k in list(cnt.values()):
    x *= k + 1
for (a, b) in list(cnt.items()):
    p = x * b // 2 % (md - 1)
    ans = ans * pow(a, p, md) % md
print(ans)
