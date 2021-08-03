from collections import Counter
n = int(input())
c = Counter(map(int, input().split()))
ans = 0
for i in c:
    if c[i] > i:
        ans += c[i] - i
    elif c[i] < i:
        ans += c[i]
print(ans)
