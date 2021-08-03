def main():
    d, l, a, b = map(int, input().split())
    l -= d
    ans = l / (a + b)
    print(ans)


main()
