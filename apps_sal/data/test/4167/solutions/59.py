def main():
    (N, K) = [int(n) for n in input().split(' ')]
    mul_K = int(N / K)
    if K % 2 == 1:
        print(mul_K ** 3)
        return 0
    mul_K_half = int(2 * N / K)
    mul_K_half_but_K = mul_K_half - mul_K
    print(mul_K ** 3 + mul_K_half_but_K ** 3)
    return 0


main()
