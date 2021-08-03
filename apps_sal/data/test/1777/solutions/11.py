import collections


def rev(l):
    ret = ""
    for ch in l[::-1]:
        ret = ret + ("(" if ch == ")" else ")")
    return ret


def cnt(l):
    ret = cntimpl(l)
    if ret is None:
        ret = cntimpl(rev(l))
        if ret is not None:
            ret *= -1
    return ret


def cntimpl(l):
    q = 0
    for ch in l:
        if ch == "(":
            q += 1
        else:
            q -= 1
            if q < 0:
                return None
    return q

###


n = int(input())
s = [input() for _ in range(n)]

#print(n, s)

v = [cnt(x) for x in s]

# print(v)

v = [x for x in v if x is not None]
v.sort()
v = collections.deque(v)

# print(v)

ans = 0
while len(v) > 1:
    if v[0] == -v[-1]:
        ans += 1
        v.pop()
        v.popleft()
    elif abs(v[0]) > abs(v[-1]):
        v.popleft()
    else:
        v.pop()

print(ans)
