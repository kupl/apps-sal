def main():
    n = int(input())
    l = list(sorted(map(int, input().split())))
    ans = 0
    for i in range(0, 2 * n, 2):
        ans += l[i]
    print(ans)


main()
