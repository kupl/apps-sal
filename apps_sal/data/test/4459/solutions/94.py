from collections import Counter
n = int(input())
a = list(map(int, input().split()))
ca = Counter(a)
ans = 0
for k in list(ca.keys()):
    if ca[k] > k:
        ans += ca[k] - k
    elif ca[k] < k:
        ans += ca[k]
print(ans)
