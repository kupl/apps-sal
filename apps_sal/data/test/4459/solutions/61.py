import collections
n = int(input())
aa = list(map(int, input().split()))
cc = collections.Counter(aa)
cnt = 0
for c in list(cc.items()):
    if c[0] > c[1]:
        cnt += c[1]
    elif c[0] == c[1]:
        continue
    elif c[0] < c[1]:
        cnt += c[1] - c[0]
print(cnt)
