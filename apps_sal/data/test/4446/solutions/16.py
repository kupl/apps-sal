
def main():
    n, a, b, k = list(map(int, input().split()))
    arr = [(a + b - 1) // a if x % (a + b) == 0 else (x % (a + b) - 1) // a for x in map(int, input().split())]
    arr.sort()
    ans = 0
    for x in arr:
        if(k < x):
            break
        k -= x
        ans += 1
    print(ans)


def __starting_point():
    main()


__starting_point()
