def solve(a, b, s, n):
    if not a[0]:
        return "NO"
    if a[s - 1]:
        return "YES"
    if b[s - 1]:
        for i in range(s, n):
            if a[i] and b[i]:
                return "YES"
    return "NO"


def main():
    n, s = [int(i) for i in input().split()]
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    print(solve(a, b, s, n))


main()
