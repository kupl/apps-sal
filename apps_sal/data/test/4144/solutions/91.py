# １０＾９＋７で割った余りを出力
n = int(input())
mod = 10**9 + 7
# pow(5,2) = 25 べき乗計算 pow()の第三引数は剰余
ans = pow(10, n, mod) - 2 * pow(9, n, mod) + pow(8, n, mod)
print((ans % mod))
