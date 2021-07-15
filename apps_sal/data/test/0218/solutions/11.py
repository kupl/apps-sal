def main():
    n, p, q = list(map(int, input().split()))
    s = input()

    for i in range(0, n + 1):
        for j in range(0, n + 1):
            if p * i + q * j == n:
                print(i + j)
                for k in range(i):
                    print(s[:p])
                    s = s[p:]
                for k in range(j):
                    print(s[:q])
                    s = s[q:]
                return 0

    print(-1)
    return 0

main()

