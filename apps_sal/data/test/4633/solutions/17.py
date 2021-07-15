def solve(n, s):
    dns = [ord(x)-ord('0') for x in str(n)]
    if sum(dns) <= s:
        return 0
    m = len(dns)
    for i, d in enumerate(dns):
        if d >= s:
            return 10**(m-i) - (n % (10**(m-i)))
        s -= d
    return 42


for _ in range(int(input())):
    n, s = [int(x) for x in input().split()]
    print(solve(n, s))

