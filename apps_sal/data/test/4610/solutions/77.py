from collections import Counter
(n, k) = map(int, input().split())
a = list(map(int, input().split()))
a1 = Counter(a).most_common()
num = 0
if k < len(a1):
    for i in range(1, len(a1) - k + 1):
        num += a1[-i][1]
    print(num)
else:
    print(0)
