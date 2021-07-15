import sys

input = sys.stdin.readline
a, b, x= map(int, input().split())
max_number = 10**9 + 1
min_number = 0

def is_ok(n):
    money = a * n + b * len(str(n))
    if money <= x:
        return True
    else:
        return False
    


'''
初期値のng,okを受け取り,is_okを満たす最小(最大)のokを返す
まずis_okを定義すべし
ng ok は  とり得る最小の値-1 とり得る最大の値+1
最大最小が逆の場合はよしなにひっくり返す
'''
def meguru_bisect(ng, ok):
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok

ans = meguru_bisect(max_number,min_number)
print(ans)
