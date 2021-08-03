def main():
    s = input()
    for k in range(len(s) // 2 + 1, len(s)):
        if s[:k] == s[len(s) - k:]:
            print("YES", s[:k], sep='\n')
            return 0
    print("NO")


main()
