n = int(input())
#n, W = map(int, input().split())
al = list(map(int, input().split()))
#al=[list(input()) for i in range(n)]


def div2(v, a):
    res = 0
    if v == 0:
        return res
    while v % a == 0:
        v = v // a
        res += 1
    return res


ans = 0
for a in al:
    ans += div2(a, 2)
print(ans)
