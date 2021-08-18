def main():
    s = list(input())

    for _ in range(len(s)):
        s.pop()
        if len(s) % 2 == 0:
            p = len(s) // 2
            if s[0:p] == s[p:]:
                print(len(s))
                return


if __name__ == "__main__":
    main()
