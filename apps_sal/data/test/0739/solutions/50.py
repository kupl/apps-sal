# Atcoder Problem Solving
# F - Takahashi's Basics in Education and Learning
import math
L, A, D, mod = map(int, input().split())
que = []

ans = 0
# 1桁、......20桁のグループに分類する
for i in range(1, 22):
    #10**(i-1) <= A+D*(j) < 10**(i)
    if (10**(i-1)-A+D) % D == 0:
        lowest = max(1, (10**(i-1)-A+D)//D)
    else:
        lowest = max(1, (10**(i-1)-A+D)//D+1)
    highest = 0
    if (10**i-A+D) % D == 0:
        highest = min((10**i-A+D)//D-1, L)

    else:
        highest = min((10**i-A+D)//D, L)

    if 1 <= lowest <= highest:
        que.append((i, lowest, highest))


def poly_sum(X, N, mod):
    # return X^N +    .... X^1+1 mod
    # O(logN)
    if N == 0:
        return 1
    if N == 1:
        return (X+1) % mod
    else:
        if N % 2 == 0:
            tmp_res = poly_sum(X, N//2, mod)
            return ((pow(X, N//2, mod)+1)*tmp_res-pow(X, N//2, mod)) % mod

        elif N % 2 != 0:
            tmp_res = poly_sum(X, N//2, mod)
            return (pow(X, N//2+1, mod)+1)*tmp_res % mod


def sum_of_poly_sum(X, N, mod):
    # return poly_sum(X,N,mod)+ poly_sum(X,N-1,mod) +poly_sum(X,N-2,mod) +.....  + poly_sum(X,1,mod) + poly_sum(X,0,mod)
    # O(logN*logN)
    if N == 0:
        return poly_sum(X, 0, mod)
    elif N == 1:
        return (poly_sum(X, 1, mod)+poly_sum(X, 0, mod)) % mod
    else:
        return ((sum_of_poly_sum(X, (N-1)//2, mod))*(pow(X, N//2+1, mod)+1)+(N//2+1)*poly_sum(X, N//2, mod)) % mod


def find_mod(length, lowest, highest, mod):
    # length 桁　の lowest 項目から highest 項目における連結巨大数のmodular
    X = pow(10, length, mod)
    if highest > lowest:
        base = (A+D*(lowest-1))*poly_sum(X, highest-lowest, mod) + \
            D*sum_of_poly_sum(X, highest-lowest - 1, mod)
    elif highest == lowest:
        base = A+D*(lowest-1)
    return base % mod


que.reverse()

digits = 0
for length, lowest, highest in que:
    ans += find_mod(length, lowest, highest, mod)*pow(10, digits, mod)
    ans %= mod
    digits += length*(highest+1-lowest)

print(ans % mod)
