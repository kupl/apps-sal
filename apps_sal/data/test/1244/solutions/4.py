from collections import Counter
n = int(input())
lst = [int(x) for x in input().split()]
c = Counter(lst)
print('YES' if c.most_common(1)[0][1] * 2 - 1 <= n else 'NO')
