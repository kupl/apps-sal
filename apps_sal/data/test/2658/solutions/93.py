def delete_head_zeros(n):
    n = str(n)
    l = len(n)
    if "." in n:
        l = n.find(".")
    head_zeros = 0
    for i in range(l - 1):
        if n[i] == "0":
            head_zeros += 1
        else:
            break

    return n[head_zeros:]


def bigint_compare(a, b):
    a = delete_head_zeros(a)
    b = delete_head_zeros(b)
    if len(a) > len(b):
        return 1
    elif len(a) < len(b):
        return -1
    else:
        if a > b:
            return 1
        elif a < b:
            return -1
        else:
            return 0


def bigint_plus(a, b):
    a = str(a)
    b = str(b)

    d = max([len(a), len(b)])
    a = '0' * (d - len(a)) + a
    b = '0' * (d - len(b)) + b

    ans = ""
    carry = 0
    for i in range(d):
        s = int(a[-i - 1]) + int(b[-i - 1]) + carry
        carry = s // 10
        ans = str(s % 10) + ans
    else:
        if carry:
            ans = str(carry) + ans

    return ans


def bigint_minus(a, b):
    a = str(a)
    b = str(b)
    M = []
    m = []
    sign = ""

    if len(a) > len(b) or (len(a) == len(b) and a >= b):
        [M, m] = [a, b]
    else:
        [M, m] = [b, a]
        sign = "-"
    m = '0' * (len(M) - len(m)) + m

    ans = ""
    borrow = 0
    for i in range(len(M)):
        s = int(M[-i - 1]) - int(m[-i - 1]) - borrow
        if s < 0:
            borrow = 1
            s += 10
        else:
            borrow = 0
        ans = str(s) + ans

    return sign + delete_head_zeros(ans)


def bigint_multiply(a, b):
    a = str(a)
    b = str(b)

    md = []
    for j in range(len(b)):
        carry = 0
        mj = ""
        for i in range(len(a)):
            m = int(a[-i - 1]) * int(b[-j - 1]) + carry
            carry = m // 10
            mj = str(m % 10) + mj
        else:
            if carry:
                mj = str(carry) + mj
        md.append(mj)

    ans = 0
    for k in range(len(md)):
        ans = bigint_plus(md[k] + "0" * k, ans)

    return ans


def bigint_divide(a, b, d=0):
    a = str(a)
    b = str(b)
    d = int(d)
    if d < 0:
        d = 0

    ans = ""
    r = ""
    for i in range(len(a) + d):
        q = 0
        if i < len(a):
            r += a[i]
        elif i == len(a):
            ans += "."
            r += "0"
        else:
            r += "0"

        if bigint_compare(r, b) == -1:
            ans += str(q)
        else:
            while bigint_compare(r, b) >= 0:
                r = bigint_minus(r, b)
                q += 1
            ans += str(q)

    return delete_head_zeros(ans)


def main():
    N, K = input().split(" ")
    A = [int(a) - 1 for a in input().split(" ")]
    visited = [0] * int(N)
    towns = []
    now = 0
    while visited[now] == 0:
        towns.append(now)
        visited[now] = 1
        now = A[now]
    else:
        loop_begin_idx = towns.index(now)
        loop_end_idx = len(towns) - 1
        loop_n = loop_end_idx - loop_begin_idx + 1
    if int(K) < len(towns):
        print((towns[int(K)] + 1))
        return 0
    K_from_loop = bigint_minus(K, loop_begin_idx)
    q = bigint_divide(K_from_loop, loop_n)
    r = bigint_minus(K_from_loop, bigint_multiply(loop_n, q))
    print((towns[loop_begin_idx + int(r)] + 1))


main()
