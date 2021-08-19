from collections import Counter


def read():
    return int(input())


def readmap():
    return map(int, input().split())


def readlist():
    return list(map(int, input().split()))


(n, m) = readmap()
A = readlist()
c = Counter(A)
freq = []
for v in c.values():
    freq.append(v)
freq.sort(reverse=True)


def ok(i):
    j = n
    for f in freq:
        j -= f // i
    if j <= 0:
        return True
    else:
        return False


for i in reversed(range(1, m + 1)):
    if ok(i):
        print(i)
        quit()
print(0)
