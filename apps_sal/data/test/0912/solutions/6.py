def main():
    for _ in range(int(input())):
        n, s, k = map(int, input().split())
        a = list(map(int, input().split()))

        if s not in a:
            print(0)
            continue

        ans = 1
        t1 = s + 1
        t2 = s - 1
        for i in range(n):
            if t2 > 0:
                if t2 not in a:
                    break
                t2 -= 1
            if t1 <= n:
                if t1 not in a:
                    break
                t1 += 1
            ans += 1

        print(ans)


main()
