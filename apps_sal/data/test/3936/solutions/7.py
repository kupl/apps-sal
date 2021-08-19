import sys

N = int(sys.stdin.readline())
S = ["", ""]
S[0] = sys.stdin.readline().strip()
S[1] = sys.stdin.readline().strip()

mod = 10**9 + 7

pre = [S[0][0], S[1][0]]
ans = 3
if S[0][0] != S[1][0]:
    ans *= 2
# print(0, 1, ans)

for i in range(1, N):
    # 一つ前と同じ場合
    if pre[0] == S[0][i] and pre[1] == S[1][i]:
        continue

    if pre[0] == pre[1]:
        ans *= 2
        ans %= mod
        # 縦詰が連続
        # if S[0][i] == S[1][i]:
        #     ans *= 2
        #     ans %= mod
        # else:
        #     ans *= 2
        #     ans %= mod
    else:
        # 1パターンしかない
        if S[0][i] == S[1][i]:
            ans *= 1
        else:
            ans *= 3
            ans %= mod

    # print(ans)

    pre[0] = S[0][i]
    pre[1] = S[1][i]

print(ans)
