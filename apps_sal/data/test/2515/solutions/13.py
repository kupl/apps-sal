def get_sieve_of_eratosthenes(n):
    if not isinstance(n, int):
        raise TypeError('n is int type.')
    if n < 2:
        raise ValueError('n is more than 2')
    prime = [2]
    limit = int(n**0.5)
    data = [i + 1 for i in range(2, n, 2)]
    while True:
        p = data[0]
        if limit < p:
            return prime + data
        prime.append(p)
        data = [e for e in data if e % p != 0]


MAX = pow(10, 5) + 10
A = get_sieve_of_eratosthenes(MAX)
A = set(A)
S = [0]
for i in range(1, MAX):
    if i in A and (i + 1) % 2 == 0 and (i + 2) // 2 in A:
        temp = S[-1] + 1
    else:
        temp = S[-1]
    S.append(temp)
Q = int(input())
for i in range(Q):
    l, r = map(int, input().split())
    ans = S[r] - S[l - 1]
    print(ans)
