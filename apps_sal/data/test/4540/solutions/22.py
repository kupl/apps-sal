def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.append(0)

    base = abs(a[0])
    for i in range(n):
        base += abs(a[i + 1] - a[i])

    ans = []
    for i in range(n):
        if (a[i] - a[i - 1]) * (a[i + 1] - a[i]) >= 0:
            ans.append(base)
        else:
            ans.append(base - 2 * min(abs(a[i] - a[i - 1]), abs(a[i + 1] - a[i])))

    for i in ans:
        print(i)


main()
