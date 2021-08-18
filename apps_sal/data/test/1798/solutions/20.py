from collections import defaultdict
def get(): return (list(map(int, input().split())))


def isap(l):
    if len(l) < 2:
        return len(l) - 1
    d = l[1] - l[0]
    i = 0
    n = len(l)
    while i < n - 1:
        if l[i + 1] - l[i] != d:
            return -1
        i += 1
    return d


o = 33
n = int(input())
l = get()
d = defaultdict(lambda: [])
for j, i in enumerate(l):
    d[i].append(j)
ans = {}
for x in d:
    t = isap(d[x])
    if t != -1:
        ans[x] = t
print(len(ans))
for i in sorted(ans):
    print(i, ans[i])
