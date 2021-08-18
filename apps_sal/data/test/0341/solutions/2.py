
N, K = map(int, input().split())


R, S, P = map(int, input().split())
T = input()
win = {"r": ["p", P], "s": ["r", R], "p": ["s", S]}

hands = []
tot = 0
for i, c in enumerate(T):
    if i >= K and win[c][0] == hands[i - K]:
        hands.append("anything")
        continue
    hands.append(win[c][0])
    tot += win[c][1]

print(tot)
