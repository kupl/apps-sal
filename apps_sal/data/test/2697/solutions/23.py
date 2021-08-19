MAX = 10000
prefix = [0] * (MAX + 1)


def buildPrefix():
    prime = [1] * (MAX + 1)
    p = 2
    while p * p <= MAX:
        if prime[p] == 1:
            i = p * 2
            while i <= MAX:
                prime[i] = 0
                i += p
        p += 1
    for p in range(2, MAX + 1):
        prefix[p] = prefix[p - 1]
        if prime[p] == 1:
            prefix[p] += 1


def query(L, R):
    return prefix[R] - prefix[L - 1]


buildPrefix()
L = 1
R = int(input())
print(query(L, R))
