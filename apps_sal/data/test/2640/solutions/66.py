def main():
    NEG = -10**6
    H, W = list(map(int, input().split()))
    S = [input() for _ in range(H)]
    T = [[NEG] * W for _ in range(H)]
    for w in range(W):
        b = NEG
        for h in range(H):
            if S[h][w] == '.':
                if b == NEG:
                    b = h
            else:
                if b != NEG:
                    for j in range(b, h):
                        T[j][w] = h - b
                    b = NEG
        if b != NEG:
            for j in range(b, h + 1):
                T[j][w] = h + 1 - b
    m = 0
    for s, t in zip(S, T):
        b = NEG
        for i in range(len(s)):
            if s[i] == '#':
                if b != NEG:
                    m = max(m, i - b - 1 + max(t[b:i]))
                    b = NEG
            else:
                if b == NEG:
                    b = i
        if b != NEG:
            m = max(m, i - b + max(t[b:i + 1]))
    print(m)

main()

