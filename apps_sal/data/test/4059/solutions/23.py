def main():
    n = int(input())
    ans, i = 0, 1
    while i < n:
        ans += (n - 1) // i
        i += 1
    print(ans)


main()
