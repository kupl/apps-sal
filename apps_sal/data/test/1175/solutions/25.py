L, R = list(map(int, input().split()))
ans = 0
mod = 10 ** 9 + 7
for d in range(62):  # 最上位 bit
    # dp[n] := n 桁目まで見た時に条件を満たすものが何個あるか
    # dp_small[n] := n 桁目まで見た時に、l と x が n 桁目まで一致していて条件を満たすものが何個あるか
    l = max(1<<d, L)
    r = min((2<<d)-1, R)
    if l > r:
        continue
    dp_small = [0] * (d+2)
    dp_ok = [0] * (d+2)
    dp_large = [0] * (d+2)
    dp_small_large = [0] * (d+2)
    dp_small_large[0] = 1
    for n in range(1, d+2):
        i = d-n+1
        dp_ok[n] = dp_ok[n-1] * 3 \
                 + (dp_small[n-1] if l>>i&1==0 else 0) \
                 + (dp_large[n-1] if r>>i&1 else 0)
        dp_small[n] = dp_small[n-1] * (1 if l>>i&1 else 2) \
                    + (dp_small_large[n-1] if l>>i&1 < r>>i&1 else 0)
        dp_large[n] = dp_large[n-1] * (2 if r>>i&1 else 1) \
                    + (dp_small_large[n-1] if l>>i&1 < r>>i&1 else 0)
        dp_small_large[n] = dp_small_large[n-1] if l>>i&1 <= r>>i&1 else 0
    a = dp_ok[d+1] + dp_large[d+1] + dp_small[d+1] + dp_small_large[d+1]
    ans += a
    # print(f"d={d},a={a},l={l},r={r}")
    # print(f"dp_ok={dp_ok}")
    # print(f"dp_small={dp_small}")
    # print(f"dp_large={dp_large}")
    # print(f"dp_small_large={dp_small_large}")
    # print()
print((ans % mod))

