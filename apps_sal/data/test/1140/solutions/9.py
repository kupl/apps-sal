from collections import Counter
n = int(input())
b = list(map(int, input().split()))
d = Counter(b)
min1 = min(b)
max1 = max(b)
if max1 == min1:
    print(0, n * (n - 1) // 2)
    return
diff = max1 - min1
no_ways = d[max1] * d[min1]
print(diff, no_ways)
