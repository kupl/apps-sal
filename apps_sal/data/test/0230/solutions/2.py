from collections import defaultdict as dd
N = int(input())
s = str(input())
maxlen = N // 2


def solve(tgt):
    dic = dd(int)
    st = s[tgt:2 * tgt]
    dic[st] += 1
    ls = [st]
    for char in s[2 * tgt:]:
        st = st[1:] + char
        dic[st] += 1
        ls.append(st)
    st = s[:tgt]
    if dic[st] > 0:
        return True
    dic[ls[0]] -= 1
    for i, char in enumerate(s[tgt:N - tgt]):
        st = st[1:] + char
        if dic[st] > 0:
            return True
        dic[ls[i + 1]] -= 1
    return False


ng = maxlen + 1
ok = 0
while ng - ok > 1:
    tgt = (ok + ng) // 2
    if solve(tgt):
        ok = tgt
    else:
        ng = tgt
print(ok)
