N, K = map(int, input().split())
A = [int(i) for i in input().split()]

def f(length, ls):
    cur = 0
    for a in ls:
        if a%length == 0:
            cur += a//length - 1
        else:
            cur += a//length
    if cur <= K:
        return True
    else:
        return False

ok, ng = max(A), 0
while abs(ok - ng) > 1:
    z = (ok+ng)//2
    if f(z, A) == True:
        ok = z
    else:
        ng = z
print(ok)
