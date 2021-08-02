import collections
a = int(input())
b = [int(input()) for i in range(a)]

n = collections.Counter(b)
m, ans = zip(*n.most_common())
ans = [i for i in ans if i % 2 == 1]
print(len(ans))
