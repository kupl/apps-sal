

MOD = 10**9 + 7
def I(): return list(map(int, input().split()))


t, = I()
while t:
    t -= 1
    n, k = I()
    s = ''.join([chr(i) for i in range(97, 97 + k)])
    print(s * (n // k) + s[:n % k])
