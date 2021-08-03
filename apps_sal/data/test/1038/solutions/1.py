import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

a, b = list(map(int, input().split()))

# 0からnまでのXOR和


def xor_sum(n):
    ans = 0
    # XORで1になる組数を求める
    if n % 2:
        # 奇数の時は切り上げて偶奇判定
        ans = ((n + 1) // 2) % 2
    else:
        # 偶数の時はnとのXORを返す
        ans = (n // 2) % 2
        ans ^= n
    return ans


print((xor_sum(b) ^ xor_sum(a - 1)))
