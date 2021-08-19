from collections import Counter


def read():
    return list(map(int, input().split()))


(n, x) = read()
a = list(read())
c = Counter()
for i in a:
    c[i] += 1
cnt = 0
for i in a:
    cnt += c[i ^ x] - (x == 0)
cnt //= 2
print(cnt)
