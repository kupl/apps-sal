n = int(input())
ok, ng = 1, n+1

def is_ok(x):
    if x*(x+1)//2 <= n+1: return True
    else: return False

while abs(ok-ng) > 1:
    mid = abs(ok+ng)//2
    if is_ok(mid): ok = mid
    else: ng = mid

print(n+1-ok)
