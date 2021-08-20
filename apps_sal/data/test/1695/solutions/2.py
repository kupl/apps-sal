from collections import Counter
(n, m) = list(map(int, input().split()))
s = [input() for _ in range(n)]
s = [*list(zip(*s))]
a = [*list(map(int, input().split()))]
print(sum((x.most_common(1)[0][1] * y for (x, y) in zip(list(map(Counter, s)), a))))
