N, K = map(int, input().split())
A = list(map(int, input().split()))


def f(x, n):
    i = 0
    while x != 0:
        cnt_bit[i] += x % abs(n)
        if n < 0:
            x = - ((-x) // n)
        else:
            x //= n
        i += 1


def base(x, n):
    ret = []
    while x != 0:
        ret.append(x % abs(n))
        if n < 0:
            x = - ((-x) // n)
        else:
            x //= n
    return ret


cnt_bit = [0] * 50
Flag = True

for a in A:
    f(a, 2)

B = base(K, 2)
M = len(B)

for i in range(M):
    c1, c0 = cnt_bit[M - 1 - i], N - cnt_bit[M - 1 - i]
    if Flag:
        if c1 >= c0:
            if B[M - 1 - i] == 1:
                Flag = False
            B[M - 1 - i] = 0
    else:
        if c1 >= c0:
            B[M - 1 - i] = 0
        else:
            B[M - 1 - i] = 1

if K == 0:
    k = 0
else:
    k = int("".join(map(str, reversed(B))), 2)

ans = 0
for a in A:
    ans += a ^ k

print(ans)
