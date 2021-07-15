# coding: utf-8

# https://atcoder.jp/contests/abc121


def main():
    A, B = list(map(int, input().split()))

    def xor_1_to_x(x):
        output = [0] * 40

        for k in range(40):
            output[k] = (2**k)*((x+1)//(2**(k+1)))
            output[k] += max(0, (x+1) - ((2**(k+1))*((x+1)//(2**(k+1))) + (2**k)))

        return output

    xor_B = xor_1_to_x(B)
    xor_A_m1 = xor_1_to_x(A-1)
    xor_AtoB = [None] * 40
    for k in range(40):
        xor_AtoB[k] = xor_B[k] - xor_A_m1[k]
        xor_AtoB[k] %= 2

    ans = 0
    for k in range(40):
        ans += xor_AtoB[k] * (2**k)

    return ans


print((main()))

