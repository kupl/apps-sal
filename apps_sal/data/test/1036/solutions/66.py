def solve(S):
    tbl = {80: {80: 80, 82: 80, 83: 83}, 82: {80: 80, 82: 82, 83: 82}, 83: {80: 83, 82: 82, 83: 83}}
    if len(S) % 2 == 1:
        S = S * 2
    S_ = []
    for i in range(int(len(S) / 2)):
        S_.append(tbl[S[i * 2]][S[i * 2 + 1]])
    return S_


def main():
    (N, K) = [int(x) for x in input().split()]
    S = [ord(x) for x in list(input())]
    for k in range(K):
        S = solve(S)
    print(chr(S[0]))


main()
