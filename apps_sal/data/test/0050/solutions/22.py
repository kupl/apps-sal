def gi(): return list(map(int, input().strip().split()))


n, m, r = gi()
l = gi()
ll = gi()
ans = (r // min(l)) * max(ll) + r % min(l)
if ans < r:
    ans = r
print(ans)
