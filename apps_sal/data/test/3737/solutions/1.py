def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    worst = a[0]
    best = a[-1]
    ans = 0
    for x in a:
        if worst < x and x < best:
            ans += 1

    print(ans)


main()
