def kk(): return map(int, input().split())
def ll(): return list(kk())


def dp(ls):
    if sorted(ls) == ls:
        return len(ls)
    return max(dp(ls[:len(ls) // 2]), dp(ls[len(ls) // 2:]))


_ = input(), print(dp(ll()))
