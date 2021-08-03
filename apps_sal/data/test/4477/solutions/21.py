def main():
    x = int(input())
    n = int(str(x)[0])
    l = len(str(x))
    ans = 10 * (n - 1)
    ans += l * (l + 1) // 2
    print(ans)


for _ in range(int(input())):
    main()
