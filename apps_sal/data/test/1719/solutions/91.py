from collections import defaultdict
MOD = 10**9 + 7

N = int(input())

dp = [defaultdict(int) for x in range(N + 1)]
dp[0][''] = 1


def sol(s):
    if s.find('ABC') != -1:  # 見つかった場合
        return False
    L = len(s)
    for i in range(L - 1):
        li = list(s)
        li[i], li[i + 1] = li[i + 1], li[i]
        t = ''.join(li)
        if t.find('ABC') != -1:
            return False
    return True


for n in range(N):
    for s, cnt in list(dp[n].items()):
        for c in 'ABCD':
            ns = s + c
            if sol(ns):
                dp[n + 1][ns[-3:]] += cnt
                dp[n + 1][ns[-3:]] %= MOD

ans = sum(dp[N].values())
ans %= MOD
print(ans)
