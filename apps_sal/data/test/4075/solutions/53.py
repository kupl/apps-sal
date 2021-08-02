# cs: c nnected switches
n, m = list(map(int, input().split()))


def get_connected_switches():
    # k s1 s2 .. sn
    lst = list(map(int, input().split()))
    lst.pop(0)  # k is not use
    return list([1 << (d - 1) for d in lst])


# cs: connected switches
cs = [get_connected_switches() for _ in range(m)]
ps = list(map(int, input().split()))

# bit全探索(0: すべてoffは不要)
ans = 0
# on: 0:消えてる、1:点いてる
# 10: 1 2  3   4
# 0b: 1 10 11, 100..
for on in range(2**n):
    ok = True
    for i in range(m):
        ct = 0
        for s in cs[i]:
            if s & on: ct += 1
        if ct % 2 != ps[i]:
            ok = False
    if ok:
        ans += 1
print(ans)
