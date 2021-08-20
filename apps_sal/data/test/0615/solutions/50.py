def main():
    N = int(input())
    A = list(map(int, input().split()))
    S = [0] * len(A)
    s = 0
    for (i, a) in enumerate(A):
        s += a
        S[i] = s
    l = 0
    b = 2
    m = S[-1]
    for c in range(1, N - 2):
        (p, q) = (S[l], S[c] - S[l])
        while l + 1 < c:
            (pn, qn) = (S[l + 1], S[c] - S[l + 1])
            if abs(pn - qn) >= abs(p - q):
                break
            (p, q) = (pn, qn)
            l += 1
        if b <= c:
            b = c + 1
        (r, s) = (S[b] - S[c], S[-1] - S[b])
        while b + 1 < N - 1:
            (rn, sn) = (S[b + 1] - S[c], S[-1] - S[b + 1])
            if abs(rn - sn) >= abs(r - s):
                break
            (r, s) = (rn, sn)
            b += 1
        m = min(m, max(p, q, r, s) - min(p, q, r, s))
    return m


print(main())
