def main():
    n = int(input())
    s = [int(input()) for _ in range(n)]
    s.sort()

    if sum(s) % 10 != 0:
        print(sum(s))
    else:
        for i in range(n):
            if s[i] % 10 != 0:
                print(sum(s) - s[i])
                return
        else:
            print(0)


if __name__ == "__main__":
    main()
