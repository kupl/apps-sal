INF = float('inf')
(n, k) = list(map(int, input().split()))
a = list(map(int, input().split()))


def get_divisors(num):
    (f_divs, l_divs) = ([], [])
    for i in range(1, int(num ** 0.5) + 1):
        if not num % i:
            f_divs.append(i)
            if i != num // i:
                l_divs.append(num // i)
    return f_divs + l_divs[::-1]


divs = get_divisors(sum(a))
ans = 1


def evl(d):
    rem = [x % d for x in a]
    rem.sort()
    s = sum(rem)
    c = 0
    for (i, x) in enumerate(rem):
        c += x
        if c == d * (n - i - 1) - (s - c):
            return c <= k
    return False


for d in divs[::-1]:
    if evl(d):
        print(d)
        break
