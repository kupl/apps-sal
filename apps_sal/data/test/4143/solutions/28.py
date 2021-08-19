N, A, B, C, D, E = [int(input()) for _ in range(6)]

# 1 => 2: A
# 2 => 3: B
# 3 => 4: C
# 4 => 5: D
# 5 => 6: E

# ボトルネックが全体を支配する！
# 最初からボトルネックの速度で移動するとしてOK
ans = -(-N // min(A, B, C, D, E)) + 4
print(ans)
