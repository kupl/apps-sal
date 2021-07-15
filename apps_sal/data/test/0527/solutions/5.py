S = input()
T = input()

n = len(S)

al = [chr(c) for c in range(ord("a"), ord("a")+26)]
x = {a: [] for a in al}

for i in range(len(S)):
    for a in al:
        if a == S[i]:
            x[a].append(i)

def is_ok(arg):
    # 条件を満たすかどうか？問題ごとに定義
    if x[t][arg]+c*n > i:
        return True
    return False


def meguru_bisect(ng, ok):
    '''
    初期値のng,okを受け取り,is_okを満たす最小(最大)のokを返す
    まずis_okを定義すべし
    ng ok は  とり得る最小の値-1 とり得る最大の値+1
    最大最小が逆の場合はよしなにひっくり返す
    '''
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok

i = -1
c = 0
for t in T:
    if not x[t]:
        print(-1)
        break
    if x[t][-1]+c*n <= i:
        c += 1
    i = x[t][meguru_bisect(-1, len(x[t])-1)]+c*n

else:
    print(i+1)
