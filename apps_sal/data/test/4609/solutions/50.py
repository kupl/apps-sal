import collections
n = int(input())
x = [int(input()) for i in range(n)]
c = collections.Counter(x)
cc = list(c.values())
cnt = 0
for i in range(len(cc)):
    if cc[i] % 2 == 1:
        cnt += 1
print(cnt)
