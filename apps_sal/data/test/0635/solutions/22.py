gcd = lambda a, b: gcd(b, a % b) if b else a


def main():
    n, m = list(map(int, input().split()))
    arr = [0] + list(map(int, input().split()))
    brr = [0] + list(map(int, input().split()))
    if not arr[1]:
        print("NO")
        return
    if arr[m]:
        print("YES")
        return
    if brr[m]:
        for i in range(m + 1, n + 1):
            if arr[i] and brr[i]:
                print("YES")
                return
    print("NO")
    return


main()
