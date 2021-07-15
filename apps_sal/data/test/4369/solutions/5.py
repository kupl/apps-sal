def main():
    n = int(input())
    cnt = 0
    ans  = 0

    while cnt < n:
        cnt += 2
        ans += 1
    return ans

def __starting_point():
    print(main())
__starting_point()
