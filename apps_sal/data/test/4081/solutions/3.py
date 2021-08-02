def main():
    n = int(input())
    a = list(map(int, input().split()))
    i = 0
    j = n - 1
    k = 0
    mi = 0
    ans = ""
    while True:
        if a[i] < a[j]:
            if mi < a[i]:
                mi = a[i]
                i += 1
                ans += "L"
            elif mi < a[j]:
                mi = a[j]
                j -= 1
                ans += "R"
            else:
                break
        else:
            if mi < a[j]:
                mi = a[j]
                j -= 1
                ans += "R"
            elif mi < a[i]:
                mi = a[i]
                i += 1
                ans += "L"
            else:
                break
    print(len(ans))
    print(ans)
    return 0


main()
