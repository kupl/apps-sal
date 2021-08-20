def solve(A):
    N = max(A)
    primediv = list(range(N + 1))
    for p in range(2, int(N ** 0.5) + 1):
        if primediv[p] == p:
            for i in range(2 * p, N + 1, p):
                primediv[i] = p
    count = [0] * (N + 1)
    for n in A:
        while n != 1:
            p = primediv[n]
            count[p] += 1
            while primediv[n] == p:
                n //= p
    return max(1, max(count))


n = int(input())
A = [int(x) for x in input().split()]
print(solve(A))
