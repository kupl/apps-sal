from collections import Counter
n = int(input())
a = [int(input()) for i in range(n)]
c = Counter(a).values()
ans = 0
for i in c:
    if i % 2 == 1:
        ans += 1
print(ans)
