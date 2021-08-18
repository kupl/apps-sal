def gcd(a, b):

    if b == 0:
        return a
    return gcd(b, a % b)


def lucky(l_a, r_a, t_a, l_b, r_b, t_b):

    if r_b - l_b > r_a - l_a:

        thing = [l_a, r_a, l_b, r_b]

        l_a = thing[2]
        r_a = thing[3]
        l_b = thing[0]
        r_b = thing[1]

    if l_a == l_b or r_a == r_b:

        return r_b - l_b + 1

    else:

        gcdt = gcd(t_a, t_b)

        M = gcdt - ((l_a - l_b) % gcdt)
        if M % gcdt == 0:
            M = 0
        overhang = max(M + (r_b - l_b + 1) - (r_a - l_a + 1), 0)
        overlap = max(r_b - l_b + 1 - overhang, 0)

        N = gcdt - ((r_b - r_a) % gcdt)
        if N % gcdt == 0:
            N = 0
        overhang = max(0, N + (r_b - l_b + 1) - (r_a - l_a + 1))
        overlap = max(overlap, max(0, r_b - l_b + 1 - overhang))

        return overlap


while True:

    A = input().split()

    l_a = int(A[0])
    r_a = int(A[1])
    t_a = int(A[2])

    B = input().split()

    l_b = int(B[0])
    r_b = int(B[1])
    t_b = int(B[2])

    print(lucky(l_a, r_a, t_a, l_b, r_b, t_b))

    break
