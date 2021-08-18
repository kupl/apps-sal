N, K = map(int, input().split())

if K % 2 == 1:
    n = N // K
    print(n**3)
    return

n = N // (K // 2)
n_odd, n_even = (n + 1) // 2, n // 2
print(n_odd**3 + n_even**3)
