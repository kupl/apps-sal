def make_divisors(n):
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            yield i
            if i != n // i:
                yield n // i


N, K = list(map(int, input().split()))
A = tuple(map(int, input().split()))

divisors = list(make_divisors(sum(A)))
divisors.sort(reverse=True)

for divisor in divisors:
    M = [a % divisor for a in A]
    M.sort(reverse=True)
    # divisorで割った余が大きい方に貪欲に+1していく
    if sum(M[sum(M) // divisor:]) <= K:
        print(divisor)
        return
