def main():
    q = int(input())
    for i in range(q):
        t = int(input())
        ans = 0
        while t % 5 == 0:
            t = (4 * t) // 5
            ans += 1
        while t % 3 == 0:
            t = (2 * t) // 3
            ans += 1
        while t % 2 == 0:
            t //= 2
            ans += 1
        if t != 1:
            print(-1)
        else:
            print(ans)


main()
