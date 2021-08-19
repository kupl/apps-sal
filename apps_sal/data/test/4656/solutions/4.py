def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


t = int(input())
for _ in range(t):
    (n, k) = map(int, input().split())
    s = input()
    m = [0] * 26
    for a in s:
        m[ord(a) - ord('a')] += 1
    t = max(m)
    x = t * k
    while True:
        b = x // gcd(x, k)
        count = 0
        for a in m:
            count += a // b
        if count * b >= x:
            break
        x -= 1
    print(x)
