def main():
    l = int(input())
    n = 1
    while 1 << n <= l:
        n += 1
    ans = []
    for i in range(n - 1):
        ans.append([i, i + 1, 0])
        ans.append([i, i + 1, 1 << i])
    l -= 1 << n - 1
    val = 1 << n - 1
    for p in range(n - 2, -1, -1):
        if l >= 1 << p:
            ans.append([p, n - 1, val])
            val += 1 << p
            l -= 1 << p
    print(n, len(ans))
    for (a, b, c) in ans:
        print(a + 1, b + 1, c)


main()
