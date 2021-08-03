S = input()

MOD = 10 ** 9 + 7
dp, dp_a, dp_ab, dp_abc = 1, 0, 0, 0

for s in S:
    if s == 'A':
        dp_a += dp
    elif s == 'B':
        dp_ab += dp_a
    elif s == 'C':
        dp_abc += dp_ab
    else:
        dp, dp_a, dp_ab, dp_abc = dp * 3, dp_a * 3 + dp, dp_ab * 3 + dp_a, dp_abc * 3 + dp_ab
    dp %= MOD
    dp_a %= MOD
    dp_ab %= MOD
    dp_abc %= MOD
print(dp_abc)
