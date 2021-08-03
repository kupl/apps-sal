def main():
    import sys
    input = sys.stdin.readline

    n, m, k = map(int, input().split())

    if n > m or n > k:
        print("No")
    else:
        print("Yes")

    return 0


main()
