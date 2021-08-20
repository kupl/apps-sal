(N, K) = map(int, input().split())
A = list(map(int, input().split()))
max_digit = K.bit_length()


def bi(x, max_d=max_digit):
    b = bin(x)[2:]
    if len(b) < max_d:
        return '0' * (max_d - len(b)) + b
    else:
        return b[-max_digit:]


def f(x):
    return sum(map(lambda a: a ^ x, A))


B = list(map(bi, A))
count = [0] * max_digit
ans = 0
for j in range(max_digit):
    for i in range(N):
        if B[i][j] == '1':
            count[j] += 1
    if count[j] < N / 2:
        if ans + 2 ** (max_digit - j - 1) <= K:
            ans += 2 ** (max_digit - j - 1)
        else:
            continue
print(f(ans))
