
def resolve():
    def make_divisors(n):
        divisors = []
        for i in range(1, int(n ** 0.5) + 1):
            if n % i == 0:
                # divisors.append((i, n // i)) # [(1,max), (2, max-1)]
                divisors += [i,n // i]  # [1,2,3,5]
        divisors.sort()
        return divisors

    N = int(input())
    ans = 0

    # K で割り切れない時
    div1 = set(make_divisors(N-1))
    ans += len(div1) - 1

    # K で割り切れる時
    div2 = set(make_divisors(N))
    for k in div2:
        if k == 1:
            continue
        n = N
        while n % k == 0:
            n //= k
        if n % k == 1:
            ans += 1
    print(ans)

def __starting_point():
    resolve()
__starting_point()
