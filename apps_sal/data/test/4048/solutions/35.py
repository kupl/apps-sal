def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    return divisors

def main():
    N = int(input())
    d = make_divisors(N)
    d.reverse()
    ans = float('inf')
    for i in range(N):
        if len(d) == 1:
            a = d.pop()
            ans = min(ans, 2*(a-1))
            break
        if len(d) == 0:
            break
        a = d.pop()-1
        b = d.pop()-1
        ans = min(ans, a+b)
    print(ans)

def __starting_point():
    main()

__starting_point()
