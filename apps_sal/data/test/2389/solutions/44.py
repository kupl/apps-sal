def main():
    #input
    N, A, B, C = map(int, input().split())
    s = [""] * (N+1)
    for i in range(N):
        s[i] = str(input())

    #i(0, 1, ..., N-1)回目の施行が始まる前のA, B, Cの個数を
    #a[i], b[i], c[i]とする。
    #i回目の施行で選ばれる変数をdp[i]とする。
    #output
    dp = [""] * N
    a, b, c = [0]*(N+1), [0]*(N+1), [0]*(N+1)
    a[0], b[0], c[0] = A, B, C

    #s[i]がABの時
    #   a[i] + b[i] == 0 の時続行不能
    #   a[i] == 1, b[i] == 0 の時 a[i+1] = a[i]-1, b[i+1] = b[i]+1
    #   a[i] == 0, b[i] == 1 の時 a[i+1] = a[i]+1, b[i+1] = b[i]-1
    #   a[i] == 1, b[i] == 1 の時
    #       最後のターンでなければs[i+1]を見て
    #           ABならばどちらでも良い
    #           BCならばa[i+1] = a[i]-1, b[i+1] = b[i]+1
    #           ACならばa[i+1] = a[i]+1, b[i+1] = b[i]-1
    #       最後のターンであればどちらでも良い
    #   a[i] > 1, b[i] > 1の時
    #       a[i] >= b[i]ならばa[i+1] = a[i]-1, b[i+1] = b[i]+1
    #       a[i] < b[i]ならばa[i+1] = a[i]+1, b[i+1] = b[i]-1

    for i in range(N):
        if s[i] == "AB":
            if a[i] + b[i] == 0:
                print("No")
                return
            elif a[i] == 1 and b[i] == 0:
                a[i+1] = a[i] - 1
                b[i+1] = b[i] + 1
                c[i+1] = c[i]
                dp[i] = "B"
            elif a[i] == 0 and b[i] == 1:
                a[i+1] = a[i] + 1
                b[i+1] = b[i] - 1
                c[i+1] = c[i]
                dp[i] = "A"
            elif a[i] == 0 and b[i] > 1:
                a[i+1] = a[i] + 1
                b[i+1] = b[i] - 1
                c[i+1] = c[i]
                dp[i] = "A"
            elif a[i] > 1 and b[i] == 0:
                a[i+1] = a[i] - 1
                b[i+1] = b[i] + 1
                c[i+1] = c[i]
                dp[i] = "B"
            elif a[i] == 1 and b[i] == 1:
                if s[i+1] == "":
                    a[i+1] = a[i] - 1
                    b[i+1] = b[i] + 1
                    c[i+1] = c[i]
                    dp[i] = "B"
                elif s[i+1] == "AB":
                    a[i+1] = a[i] + 1
                    b[i+1] = b[i] - 1
                    c[i+1] = c[i]
                    dp[i] = "A"
                elif s[i+1] == "BC":
                    a[i+1] = a[i] - 1
                    b[i+1] = b[i] + 1
                    c[i+1] = c[i]
                    dp[i] = "B"
                elif s[i+1] == "AC":
                    a[i+1] = a[i] + 1
                    b[i+1] = b[i] - 1
                    c[i+1] = c[i]
                    dp[i] = "A"
            elif a[i] == 1 and b[i] > 1:
                a[i+1] = a[i] + 1
                b[i+1] = b[i] - 1
                c[i+1] = c[i]
                dp[i] = "A"
            elif a[i] > 1 and b[i] == 1:
                a[i+1] = a[i] - 1
                b[i+1] = b[i] + 1
                c[i+1] = c[i]
                dp[i] = "B"
            elif a[i] > 1 and b[i] > 1:
                if a[i] >= b[i]:
                    a[i+1] = a[i] - 1
                    b[i+1] = b[i] + 1
                    c[i+1] = c[i]
                    dp[i] = "B"
                elif a[i] < b[i]:
                    a[i+1] = a[i] + 1
                    b[i+1] = b[i] - 1
                    c[i+1] = c[i]
                    dp[i] = "A"
    #ここまでで一段落。
        elif s[i] == "BC":
            if b[i] + c[i] == 0:
                print("No")
                return
            elif b[i] == 1 and c[i] == 0:
                b[i+1] = b[i] - 1
                c[i+1] = c[i] + 1
                a[i+1] = a[i]
                dp[i] = "C"
            elif b[i] == 0 and c[i] == 1:
                b[i+1] = b[i] + 1
                c[i+1] = c[i] - 1
                a[i+1] = a[i]
                dp[i] = "B"
            elif b[i] == 0 and c[i] > 1:
                b[i+1] = b[i] + 1
                c[i+1] = c[i] - 1
                a[i+1] = a[i]
                dp[i] = "B"
            elif b[i] > 1 and c[i] == 0:
                b[i+1] = b[i] - 1
                c[i+1] = c[i] + 1
                a[i+1] = a[i]
                dp[i] = "C"
            elif b[i] == 1 and c[i] == 1:
                if s[i+1] == "":
                    b[i+1] = b[i] - 1
                    c[i+1] = c[i] + 1
                    a[i+1] = a[i]
                    dp[i] = "C"
                elif s[i+1] == "BC":
                    b[i+1] = b[i] + 1
                    c[i+1] = c[i] - 1
                    a[i+1] = a[i]
                    dp[i] = "B"
                elif s[i+1] == "AC":
                    b[i+1] = b[i] - 1
                    c[i+1] = c[i] + 1
                    a[i+1] = a[i]
                    dp[i] = "C"
                elif s[i+1] == "AB":
                    b[i+1] = b[i] + 1
                    c[i+1] = c[i] - 1
                    a[i+1] = a[i]
                    dp[i] = "B"
            elif b[i] == 1 and c[i] > 1:
                b[i+1] = b[i] + 1
                c[i+1] = c[i] - 1
                a[i+1] = a[i]
                dp[i] = "B"
            elif b[i] > 1 and c[i] == 1:
                b[i+1] = b[i] - 1
                c[i+1] = c[i] + 1
                a[i+1] = a[i]
                dp[i] = "C"
            elif b[i] > 1 and c[i] > 1:
                if b[i] >= c[i]:
                    b[i+1] = b[i] - 1
                    c[i+1] = c[i] + 1
                    a[i+1] = a[i]
                    dp[i] = "C"
                elif b[i] < c[i]:
                    b[i+1] = b[i] + 1
                    c[i+1] = c[i] - 1
                    a[i+1] = a[i]
                    dp[i] = "B"
    #ここまででもう一段落。
        elif s[i] == "AC":
            if c[i] + a[i] == 0:
                print("No")
                return
            elif c[i] == 1 and a[i] == 0:
                c[i+1] = c[i] - 1
                a[i+1] = a[i] + 1
                b[i+1] = b[i]
                dp[i] = "A"
            elif c[i] == 0 and a[i] == 1:
                c[i+1] = c[i] + 1
                a[i+1] = a[i] - 1
                b[i+1] = b[i]
                dp[i] = "C"
            elif c[i] == 0 and a[i] > 1:
                c[i+1] = c[i] + 1
                a[i+1] = a[i] - 1
                b[i+1] = b[i]
                dp[i] = "C"
            elif c[i] > 1 and a[i] == 0:
                c[i+1] = c[i] - 1
                a[i+1] = a[i] + 1
                b[i+1] = b[i]
                dp[i] = "A"
            elif c[i] == 1 and a[i] == 1:
                if s[i+1] == "":
                    c[i+1] = c[i] - 1
                    a[i+1] = a[i] + 1
                    b[i+1] = b[i]
                    dp[i] = "A"
                elif s[i+1] == "AC":
                    c[i+1] = c[i] + 1
                    a[i+1] = a[i] - 1
                    b[i+1] = b[i]
                    dp[i] = "C"
                elif s[i+1] == "AB":
                    c[i+1] = c[i] - 1
                    a[i+1] = a[i] + 1
                    b[i+1] = b[i]
                    dp[i] = "A"
                elif s[i+1] == "BC":
                    c[i+1] = c[i] + 1
                    a[i+1] = a[i] - 1
                    b[i+1] = b[i]
                    dp[i] = "C"
            elif c[i] == 1 and a[i] > 1:
                c[i+1] = c[i] + 1
                a[i+1] = a[i] - 1
                b[i+1] = b[i]
                dp[i] = "C"
            elif c[i] > 1 and a[i] == 1:
                c[i+1] = c[i] - 1
                a[i+1] = a[i] + 1
                b[i+1] = b[i]
                dp[i] = "A"
            elif c[i] > 1 and a[i] > 1:
                if c[i] >= a[i]:
                    c[i+1] = c[i] - 1
                    a[i+1] = a[i] + 1
                    b[i+1] = b[i]
                    dp[i] = "A"
                elif c[i] < a[i]:
                    c[i+1] = c[i] + 1
                    a[i+1] = a[i] - 1
                    b[i+1] = b[i]
                    dp[i] = "C"

    print("Yes")
    for v in dp:
        print(v)

def __starting_point():
    main()
__starting_point()
