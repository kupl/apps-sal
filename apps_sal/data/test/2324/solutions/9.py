P = 311
# we use two mods to reduce the chance of collision
MOD1 = int(1e9) + 7
MOD2 = int(1e9) + 9


def main():
    s = input()
    n = len(s)

    # Pre-compute
    power_1 = [0 for i in range(n + 1)]
    power_2 = [0 for i in range(n + 1)]
    mod_inv_1 = [0 for i in range(n + 1)]
    mod_inv_2 = [0 for i in range(n + 1)]
    power_1[0] = 1
    power_2[0] = 1
    mod_inv_1[0] = 1
    mod_inv_2[0] = 1

    for i in range(1, n + 1):
        power_1[i] = power_1[i - 1] * P % MOD1
        power_2[i] = power_2[i - 1] * P % MOD1
        mod_inv_1[i] = bin_exp(power_1[i], MOD1 - 2, MOD1)
        mod_inv_2[i] = bin_exp(power_2[i], MOD2 - 2, MOD2)

    # Compute hash values
    hash_1 = 0
    hash_2 = 0
    forward_hash_1 = [0 for i in range(n + 1)]
    forward_hash_2 = [0 for i in range(n + 1)]

    for i in range(1, n + 1):
        hash_1 += ord(s[i - 1]) * power_1[i]
        hash_2 += ord(s[i - 1]) * power_2[i]
        hash_1 %= MOD1
        hash_2 %= MOD2
        forward_hash_1[i] = hash_1
        forward_hash_2[i] = hash_2

    hash_1 = 0
    hash_2 = 0
    backward_hash_1 = [0 for i in range(n + 1)]
    backward_hash_2 = [0 for i in range(n + 1)]

    for i in range(1, n + 1):
        hash_1 += ord(s[n - i]) * power_1[i]
        hash_2 += ord(s[n - i]) * power_2[i]
        hash_1 %= MOD1
        hash_2 %= MOD2
        backward_hash_1[i] = hash_1
        backward_hash_2[i] = hash_2

    dp = [[0 for i in range(n + 1)] for j in range(n + 1)]
    count = [0 for i in range(n + 1)]

    for sub_len in range(1, n + 1):
        for left in range(0, n - sub_len + 1):
            right = left + sub_len - 1

            if sub_len == 1:
                dp[left][right] = 1
            elif sub_len == 2:
                if s[left] == s[right]:
                    dp[left][right] = 2
            else:
                if s[left] == s[right] and dp[left + 1][right - 1] > 0:
                    dp[left][right] = dp[left][left + sub_len // 2 - 1] + 1

            count[dp[left][right]] += 1

    for i in range(n - 1, 0, -1):
        count[i] += count[i + 1]

    for i in range(1, n + 1):
        print(count[i], end=' ')

    print()


def bin_exp(a, x, mod):
    res = 1

    while x > 0:
        if x & 1:
            res *= a
            res %= mod
        a *= a
        a %= mod
        x >>= 1

    return res


def get_forward_hash(forward_hash, mod_inv, left, right, mod):
    return (forward_hash[right + 1] - forward_hash[left] + mod) * mod_inv[left] % mod


def get_backward_hash(backward_hash, mod_inv, n, left, right):
    r_left = n - left - 1
    r_right = n - right - 1
    return (backward_hash[r_left + 1] - backward_hash[r_right] + mod) * mod_inv[r_right] % mod


def __starting_point():
    main()


__starting_point()
