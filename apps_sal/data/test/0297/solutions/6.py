from fractions import gcd as g

(n, m, k) = list(map(int, input().split()))

if (n * m * 2) % k != 0:
    print("NO")
else:
    print("YES")
    n0 = n // g(n, k)
    k //= g(n, k)
    m0 = m // g(m, k)
    k //= g(m, k)

    if k == 1:
        if n0 * 2 <= n:
            n0 *= 2
        else:
            m0 *= 2

    print(0, 0)
    print(n0, 0)
    print(0, m0)
    
    

