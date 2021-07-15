def primes2(limit):
    if limit < 2: return []
    if limit < 3: return [2]
    lmtbf = (limit - 3) // 2
    buf = [True] * (lmtbf + 1)
    for i in range((int(limit ** 0.5) - 3) // 2 + 1):
        if buf[i]:
            p = i + i + 3
            s = p * (i + 1) + i
            buf[s::p] = [False] * ((lmtbf - s) // p + 1)
    return [2] + [i + i + 3 for i, v in enumerate(buf) if v]

n = int(input())
ps = primes2(int(n**0.5) + 1)

def solve(n):
    if is_prime(n):
        return [n]
    for m in range(n - 2, n//3 - 1, -1):
        if is_prime(m):
            r = n - m
            if is_prime(r):
                return [m, r]
            for s in range(r - 2, r//2 - 1, -1):
                if is_prime(s) and is_prime(r - s):
                    return [m, s, r - s]

def is_prime(n):
    sqrt_n = int(n ** 0.5)
    for p in ps:
        if n == p:
            return True
        if n % p == 0:
            return False
        if p > sqrt_n:
            return True
    return True


ans = solve(n)
print(len(ans))
print(*ans)
