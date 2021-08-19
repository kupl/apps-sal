from collections import Counter
n = int(input())
a = list(map(int, input().split()))
l1 = [i + a[i] for i in range(n)]
l2 = [i - a[i] for i in range(n)]
c2 = Counter(l2)
ans = 0
for i in l1:
    ans += c2[i]
print(ans)
