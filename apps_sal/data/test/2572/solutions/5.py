for _ in range(int(input())):
    n, m = tuple(map(int, input().split()))
    arr = []
    for i in range(n):
        arr.append(list(map(int, input().split())))

    ans = 0
    for i in range((n + 1) // 2):
        for j in range((m + 1) // 2):
            elems = [arr[i][j]]
            a = (n % 2 == 1 and i == n // 2)
            b = (m % 2 == 1 and j == m // 2)
            if not a:
                elems.append(arr[n - i - 1][j])
            if not b:
                elems.append(arr[i][m - j - 1])
            if not a and not b:
                elems.append(arr[n - i - 1][m - j - 1])

            elems.sort()
            x = len(elems) // 2
            for k in range(len(elems)):
                if k != x:
                    ans += abs(elems[k] - elems[x])

    print(ans)

