# フェルマーの小定理
def main():
    from builtins import pow

    K = int(input())
    S = input()

    m = 1000000007

    result = 0
    t = pow(26, K, m)
    u = pow(26, -1, m) * 25 % m
    l = len(S)
    for i in range(K + 1):
        # result += pow(26, K - i, m) * mcomb(len(S) - 1 + i, i) * pow(25, i, m)
        result = (result + t) % m
        t = (t * u) % m * (l + i) * pow(i + 1, -1, m) % m
    print(result)


main()
