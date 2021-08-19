N = int(input())

"""
引き算のみ
N mod K == -1
N-1 mod K == 0
K はN-1の約数

割り算が含まれる
KはNの約数
大した個数ないので、確かめる。
"""


def make_divisors(n):
    lower_divisors, upper_divisors = [], []
    i = 1
    while i * i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n // i)
        i += 1
    return lower_divisors + upper_divisors[::-1]


A = make_divisors(N - 1)
B = make_divisors(N)
ANS = set(A)
for b in B:
    if b <= 1:
        continue
    wk = N
    while wk % b == 0:
        wk = wk // b
    if wk % b == 1:
        ANS.add(b)

print(len(ANS) - 1)  # 1を除く
