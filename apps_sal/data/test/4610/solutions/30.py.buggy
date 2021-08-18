from collections import Counter
n, k = map(int, input().split())
a = list(map(int, input().split()))
t = list(set(a))
c = sorted(Counter(a).most_common(), key=lambda x: x[1])
num = len(t) - k
if num < 0:
    print(0)
    return
else:
    ans = 0
    for i in range(num):
        ans += c[i][1]
    print(ans)
