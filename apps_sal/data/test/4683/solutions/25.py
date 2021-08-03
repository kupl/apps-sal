def cusum(a):
    cusum = [a[0]]
    for i in range(len(a) - 1):
        cusum.append(cusum[i] + a[i + 1])
    return cusum


def solve1(n, a):
    ans = 0
    mod = 10**9 + 7
    cusum_a = cusum(a)

    for i in range(n):
        ans += a[i] * (cusum_a[-1] - cusum_a[i])
        """
        print(a[i], "*",
              "(", a[i+1:], "=", (cusum_a[-1] - cusum_a[i]), ")",
              "=", a[i] * (cusum_a[-1] - cusum_a[i]))
        """
        ans %= mod

    return ans


n = int(input())
a = list(map(int, input().split(" ")))
print((solve1(n, a)))
