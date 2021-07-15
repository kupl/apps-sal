def c175(x, k, d):

    x = abs(x)
    ans = 0
    if x - k * d > 0:
        return x - k * d

    if x%d <= d-(x%d):
        ans = x%d if (k - int(x//d))%2 == 0 else d-(x%d)
    else:
        ans = d-(x%d) if (k - 1 - int(x//d)) %2 == 0 else x%d

    return ans

def main():
    x, k, d = map(int, input().split())
    print(c175(x, k, d))

def __starting_point():
    main()
__starting_point()
