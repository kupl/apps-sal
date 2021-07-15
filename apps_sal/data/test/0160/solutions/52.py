def main():
    N, K = list(map(int, input().split(' ')))
    A = list(map(int, input().split(' ')))
    # Calculate divisors of sum(A)
    S = sum(A)
    divs = list()
    n = 1
    while n ** 2 <= S:
        if S % n == 0:
            m = S // n
            if n != m:
                divs.extend([n, m])
            else:
                divs.append(n)
        n += 1
    divs.sort(reverse=True)
    # calc answer
    ans = S
    for d in divs:
        B = [a % d for a in A]
        B.sort(reverse=True)
        t = sum(B) // d
        k = sum(B) - sum(B[:t])
        if d == 1:
            k = 0
        if k <= K:
            ans = d
            break
    print(ans)


def __starting_point():
    main()
__starting_point()
