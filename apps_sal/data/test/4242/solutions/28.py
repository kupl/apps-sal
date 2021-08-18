A, B, K = list(map(int, input().split()))


def make_divisors(n):
    divisors = []
    for i in range(1, int(n**.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    divisors.sort()
    return divisors


div_A = make_divisors(A)
div_B = make_divisors(B)

print((sorted(set(div_A) & set(div_B))[-K]))
