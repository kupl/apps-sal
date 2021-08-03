import collections

n = int(input())
a = list(map(int, input().split()))
cnt = 0

c = collections.Counter(a)
for i in c:
    cnt += c[i] * (c[i] - 1) // 2


for i in range(n):
    print(cnt - c[a[i]] + 1)
