from collections import Counter
n = int(input())
a = list(map(int, input().split()))
count = Counter(a)
ans = 0
for i in count.values():
    ans += i * (i - 1) // 2
for i in a:
    print(ans - (count[i] - 1))
