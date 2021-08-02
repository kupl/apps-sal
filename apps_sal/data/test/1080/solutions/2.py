def main():
    import sys
    input = sys.stdin.readline

    n = int(input())
    arr = list(map(int, input().split()))

    ma = max(arr)
    s = sum(arr)

    if ma * 2 > s or (s & 1):
        print("NO")
    else:
        print("YES")

    return 0


main()
