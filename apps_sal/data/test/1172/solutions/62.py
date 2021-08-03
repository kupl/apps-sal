S = input()
A = 0  # Aの数
B = 0  # ABの数
C = 0  # ABCの数
n = 1  # 通り数
mod = 10**9 + 7
for s in S:
    if s == "?":
        C = 3 * C + B
        B = 3 * B + A
        A = 3 * A + n
        n *= 3
    elif s == "A":
        A += n
    elif s == "B":
        B += A
    else:
        C += B
    A %= mod
    B %= mod
    C %= mod
    n %= mod
print(C)
