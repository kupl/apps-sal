def ii(): return int(input())
def mi(): return map(int, input().split())
def li(): return list(mi())


n, m, k = mi()
a = li()
mx = max(a)
mi = a.index(mx)
mx2 = max(a[:mi] + a[mi + 1:])

rep = m // (k + 1)
ans = rep * (k * mx + mx2)

rem = m % (k + 1)
ans += rem * mx

print(ans)
