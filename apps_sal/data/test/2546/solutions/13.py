import sys
input = sys.stdin.readline


def solve(mid):
    ans = 0
    cnt = 0
    tmp = []
    for i in range(n):
        if info[i][1] < mid:
            ans += info[i][0]
        elif mid < info[i][0]:
            ans += info[i][0]
            cnt += 1
        else:
            tmp.append(info[i][0])
    tmp.sort(reverse=True)
    nokori = (n + 1) // 2 - cnt
    for i in tmp:
        if nokori > 0:
            ans += mid
            nokori -= 1
        else:
            ans += i
    if ans <= s and nokori <= 0:
        return True
    else:
        return False


q = int(input())
ans = [0] * q
for qi in range(q):
    n, s = map(int, input().split())
    info = [list(map(int, input().split())) for i in range(n)]
    ok = 0
    ng = s + 1
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if solve(mid):
            ok = mid
        else:
            ng = mid
    ans[qi] = ok
print('\n'.join(map(str, ans)))
