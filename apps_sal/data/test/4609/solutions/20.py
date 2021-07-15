import collections

n = int(input())
a = [int(input()) for _ in range(n)]
c = collections.Counter(a)

cnt = 0
for x in c.values():
    if x % 2 == 1:
        cnt += 1
print(cnt)
