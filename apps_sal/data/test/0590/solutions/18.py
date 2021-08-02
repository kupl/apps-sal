import collections
n = int(input())
a = list(map(int, input().split()))
cnt = collections.Counter(a)
res = []
b = []
for i in range(1, n + 1):
    if i not in cnt:
        b.append(i)
b.sort(reverse=True)
s = set(a)
print(len(b))
for v in a:
    if v in cnt and cnt[v] > 1:
        t = b[-1]
        if v < t and v in s:
            res.append(v)
            s.remove(v)
        else:
            res.append(b.pop())
            cnt[v] -= 1
    else:
        res.append(v)
print(" ".join(list(map(str, res))))
