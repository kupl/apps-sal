from collections import Counter
n = int(input())
A = list(map(int, input().split()))
sum_a = sum(A)
d = Counter(A)
for _ in range(int(input())):
    (b, c) = map(int, input().split())
    temp = d[b]
    d[b] -= temp
    d[c] = d.get(c, 0) + temp
    sum_a += (c - b) * temp
    print(sum_a)
