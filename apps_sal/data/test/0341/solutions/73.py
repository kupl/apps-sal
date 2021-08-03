def decide_hand2(T, hand, i, K, N):
    if T[i] == "r":
        if i <= K - 1:
            hand[i] = "p"
        else:
            if hand[i - K] == "p":
                hand[i] = "-"
            else:
                hand[i] = "p"

    elif T[i] == "p":
        if i <= K - 1:
            hand[i] = "s"
        else:
            if hand[i - K] == "s":
                hand[i] = "-"
            else:
                hand[i] = "s"

    elif T[i] == "s":
        if i <= K - 1:
            hand[i] = "r"
        else:
            if hand[i - K] == "r":
                hand[i] = "-"
            else:
                hand[i] = "r"


def main():
    N, K = map(int, input().split())
    R, S, P = map(int, input().split())
    T = input()
    hand = ["" for _ in range(N)]

    for i in range(N):
        decide_hand2(T, hand, i, K, N)

    ans = 0
    for i in range(N):
        if hand[i] == "r":
            ans += R
        elif hand[i] == "s":
            ans += S
        elif hand[i] == "p":
            ans += P

    print(ans)


def __starting_point():
    main()


__starting_point()
