N, K = map(int, input().split())

# 余りを付け加えていく文字列を定義
ans_str = ''

# 割り算の商を表す変数を定義
n = N

while (n >= K):
    n = n // K
    ans_str += str(n % K)
    # print(f'n：{n}')
ans_str += str(n)
# print(ans_str[::-1])
print(len(ans_str))
