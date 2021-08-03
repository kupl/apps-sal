def ri(S): return [int(v) for v in S.split()]
def rii(): return ri(input())


H, A = rii()
H, r = divmod(H, A)
r = 1 if r else r
print(H + r)
