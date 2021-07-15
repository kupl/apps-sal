s = input()

MOD = 10**9 + 7

a, ab, abc, q = 0, 0, 0, 1

for x in s:
    # Aなら状態数を足す
    if x == "A":
        a += q
        a %= MOD
    # BならこれまでAだった状態数を足す
    elif x == "B":
        ab += a
        ab %= MOD
    # CならAB→ABCが完成する
    elif x == "C":
        abc += ab
        abc %= MOD
    # ?なら色々変化する
    else:
        # 状態数が3倍になり、?がC, Bのケースも足される
        abc = (abc * 3 + ab) % MOD
        ab = (ab * 3 + a) % MOD
        a = (a * 3 + q) % MOD
        q = q * 3 % MOD

print(abc % MOD)
