def name(n):
    return chr(ord('A') + n % 26) + chr(ord('a') + n // 26)


def main():
    n, k = map(int, input().split())
    arr = list(map(str, input().split()))
    if (arr.count("YES") == 0):
        for i in range(n):
            print("Max ", end="")
        return
    ans = ["" for i in range(n)]
    x = arr.index("YES")
    for i in range(k):
        ans[x + i] = name(i + x)
    for i in range(x + 1, n - k + 1):
        if (arr[i] == "YES"):
            ans[i + k - 1] = name(i + k - 1)
        else:
            ans[i + k - 1] = ans[i]

    for i in range(x - 1, -1, -1):
        if (arr[i] == "YES"):
            ans[i] = name(i)
        else:
            ans[i] = ans[i + k - 1]
    print(*ans)


main()
