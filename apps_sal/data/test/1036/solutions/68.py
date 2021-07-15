def resolve():
    N, K = map(int, input().split())
    S = input()

    def shorten(s):
        if len(s)%2==1:
            s = s*2
        ans = ""
        for i in range(0, len(s), 2):
            if s[i] == s[i+1]:
                ans = ans + s[i]
            elif (s[i], s[i+1]) == ("P", "R") or (s[i], s[i+1]) == ("R", "P"):
                ans = ans + "P"
            elif (s[i], s[i + 1]) == ("P", "S") or (s[i], s[i + 1]) == ("S", "P"):
                ans = ans + "S"
            elif (s[i], s[i + 1]) == ("R", "S") or (s[i], s[i + 1]) == ("S", "R"):
                ans = ans + "R"
        return ans
    ct = 0
    while ct < K:
        S = shorten(S)
        ct += 1

    print(S[0])
resolve()
