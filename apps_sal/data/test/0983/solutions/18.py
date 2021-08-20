def main():
    (n, p, q, r) = [int(i) for i in input().split()]
    L = [int(i) for i in input().split()]
    LR_big = [L[0]]
    LR_small = [L[0]]
    for i in range(1, len(L)):
        LR_big.append(max(L[i], LR_big[-1]))
        LR_small.append(min(L[i], LR_small[-1]))
    RL_big = [L[-1]]
    RL_small = [L[-1]]
    for i in range(len(L) - 2, -1, -1):
        RL_big.append(max(L[i], RL_big[-1]))
        RL_small.append(min(L[i], RL_small[-1]))
    RL_big = RL_big[::-1]
    RL_small = RL_small[::-1]
    '\t\n\tprint(LR_big)\n\tprint(LR_small)\n\tprint(RL_big)\n\tprint(RL_small)\n\t'
    count = -10 ** 20
    for i in range(len(L)):
        count = max(max(LR_small[i] * p, LR_big[i] * p) + L[i] * q + max(RL_small[i] * r, RL_big[i] * r), count)
    print(count)


main()
