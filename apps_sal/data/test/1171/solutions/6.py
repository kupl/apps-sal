N, K = list(map(int, input().split()))
V = list(map(int, input().split()))

max_value = -10**9
for kL in range(0, K + 1):
    for kR in range(0, K + 1):
        if kL + kR > min(N, K):
            continue
        vL = V[:kL]
        vR = []
        if kR:
            vR = V[-kR:]
        hand = list(sorted(vL + vR, reverse=True))
        rest = K - (kL + kR)
        for kD in range(rest):
            if len(hand) == 0:
                break
            if hand[-1] < 0:
                hand.pop()
            else:
                break
        value = sum(hand[:K])
        if value > max_value:
            max_value = value
print(max_value)
