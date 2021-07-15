from sys import stdin as cin

def main():
    n = int(cin.readline())
    k = int(cin.readline())
    a = int(cin.readline())
    b = int(cin.readline())
    o = 0
    if k == 1:
        print((n - 1) * a)
        return
    while n > 1:
        if n % k:
            t = n - n // k * k
            if t == n:
                t -= 1
            o += a * t
            n -= t
        else:
            t = n // k
            o += min(a * (n - t), b)
            n = t
        #print(n, o)
    print(o)

main()

