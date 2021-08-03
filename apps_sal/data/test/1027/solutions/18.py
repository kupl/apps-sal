def main():
    a = [int(i) for i in input().split(' ')]

    ans = 0
    for i in range(14):
        if (a[i] == 0):
            continue
        b = a.copy()

        k = a[i] // 14
        r = a[i] % 14
        b[i] = 0
        for j in range(14):
            b[j] += k

        for j in range(r):
            b[(i + 1 + j) % 14] += 1

        score = 0
        for x in b:
            if x % 2 == 0:
                score += x

        ans = max(ans, score)
    print(ans)


main()
