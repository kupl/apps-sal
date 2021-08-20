from collections import Counter
n = int(input())
a = list(map(int, input().split()))
c = Counter(a)
even_cnt = sum([cnt % 2 == 0 for (i, cnt) in c.items()])
if even_cnt % 2:
    print(len(c) - 1)
else:
    print(len(c))
