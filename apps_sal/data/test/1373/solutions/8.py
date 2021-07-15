# https://drken1215.hatenablog.com/entry/2020/04/20/003900
# k  個足してできる最小の整数を求める (a とする)
# k 個足してできる最大の整数を求める (b とする)
# 出来上がる整数は b−a+1 個である

N, K = map(int, input().split())
mod = 10 ** 9 + 7

ans = 0
for k in range(K, N+2):
    mx = k * (2 * N - k + 1) / 2
    mi = k * (k - 1) / 2
    add = mx - mi + 1
    ans += add
    ans %= mod
print(int(ans))
