N, K = map(int, input().split())

# 整数N を K進数 で表したとき、何桁になるかを出力
# 位取り記数法：https://xtech.nikkei.com/atcl/learning/lecture/19/00049/00001/

digit = 0

while N > 0:
    N = N // K
    digit += 1

print(digit)
