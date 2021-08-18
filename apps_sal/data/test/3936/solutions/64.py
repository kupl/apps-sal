def resolve():
    mod = 1000000007
    N = int(input())
    S = [list(input()) for _ in range(2)]

    domino_directions = []
    for i in range(N):
        if S[0][i] == S[1][i]:
            domino_directions.append("|")
            continue
        if i + 1 < N:
            if S[0][i] == S[0][i + 1]:
                domino_directions.append("-")
                i += 1
    ans = 3 if domino_directions[0] == "|" else 6
    for i in range(1, N):
        pair = "".join(domino_directions[i - 1:i + 1])

        if pair == "||" or pair == "|-":
            ans *= 2
        elif pair == "--":
            ans *= 3

        if ans > mod:
            ans %= mod
    print(ans)


resolve()
