a, b, c = map(int, input().split())

# シグマの分解公式があるようだ。自力で解けなかった。
# https://mathtrain.jp/sigma
mod = 998244353
print((a*(a+1)//2)*(b*(b+1)//2)*(c*(c+1)//2)%mod)
