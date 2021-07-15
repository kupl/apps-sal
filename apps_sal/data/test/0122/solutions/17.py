def f(aa, s):
    d = {a: i for i, a in enumerate(aa)}
    for i, a in enumerate(aa):
        if s in d and i <= d[s]:
            return True
        s -= a
        if s <= 0:
            break
    return not s


n = int(input())
aa = list(map(int, input().split()))
s, res = sum(aa), False
if not s & 1 and n > 1:
    res = f(aa, s // 2)
    if not res:
        aa.reverse()
        res = f(aa, s // 2)
print(("NO", "YES")[res])
