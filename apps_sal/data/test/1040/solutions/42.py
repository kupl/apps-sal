def resolve():
    N = int(input())
    S = list(input())
    if N < 3:
        print(N)
    else:
        now = S[:2]
        ans = 0
        for i in range(2, len(S)):
            now.append(S[i])
            if now[-3:] == ["f", "o", "x"]:
                now.pop()
                now.pop()
                now.pop()
                ans += 3

        print(N - ans)


resolve()
