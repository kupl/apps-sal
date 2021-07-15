def main():
    s = input()
    ans = len(s)
    for i in range(len(s)-1):
        if s[i] != s[i+1]:
            tmp = max(i+1, len(s)-i-1)
            ans = min(ans, tmp)
    print(ans)

def __starting_point():
    main()
__starting_point()
