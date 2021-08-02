from collections import Counter
n = int(input())
a = list(map(int, input().split()))
b = Counter(a)
ans = 0
for i in set(a):
    if b[i] < i:
        ans += b[i]
    else:
        ans += b[i] - i
print(ans)
