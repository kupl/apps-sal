USE_STDIO = False

if not USE_STDIO:
    try: import mypc
    except: pass

def gcd(x, y):
    if x % y == 0: return y
    return gcd(y, x % y)

def main():
    a, b, x, y = list(map(int, input().split(' ')))
    g = gcd(x, y)
    x, y = x // g, y // g
    ans = min(a // x, b // y)
    print(ans)

def __starting_point():
    main()




__starting_point()
