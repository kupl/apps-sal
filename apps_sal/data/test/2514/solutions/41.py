from collections import Counter
n = int(input())
a = list(map(int, input().split()))
q = int(input())
counter = Counter(a)
sum_res = sum(a)
for _ in range(q):
    (before, after) = map(int, input().split())
    sum_res -= before * counter[before]
    sum_res += after * counter[before]
    counter[after] += counter[before]
    counter[before] = 0
    print(sum_res)
