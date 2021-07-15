A, B = list(map(int, input().split()))


def prime_numbers(N):
    n = N
    res = set()
    for i in range(2, n):
        if i * i >= n: break
        if N % i != 0: continue
        while N % i == 0:
            N //= i
        res.add(i)
    res.add(N)
    res.add(1)
    return res


a = prime_numbers(A)
b = prime_numbers(B)
#print(a, b)
#print(a.intersection(b))
ans = len(a.intersection(b))
print(ans)

