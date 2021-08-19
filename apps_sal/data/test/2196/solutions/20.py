n = int(input())
s = list(map(int, input().split()))


def ins(_set, n):
    if n in _set:
        _set.remove(n)
        ins(_set, n + 1)
    else:
        _set.add(n)


ss = set()
for i in s:
    ins(ss, i)
m = max(ss)
print(m - len(ss) + 1)
