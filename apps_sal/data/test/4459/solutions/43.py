from collections import Counter
n = int(input())
alist = list(map(int, input().split()))
adic = Counter(alist)
count = 0
for k, v in adic.items():
    if int(k) <= v:
        count += (v - int(k))
    else:
        count += v
print(count)
