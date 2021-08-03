import collections

n = int(input())
abc = []

for i in range(n):
    a = list(input())
    a.sort()
    a = str(a)
    abc.append(a)

c = collections.Counter(abc)
cnt = 0

for i in c:
    num = c[i]
    if num != 1:
        cnt += num * (num - 1) // 2

print(cnt)
