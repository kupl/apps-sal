N = int(input())
W = list(map(int, input().split()))

abs_list = []  # 絶対値リスト
for T in range(N - 1):
    # print(W[:T+1],W[T+1:])
    S1 = sum(W[:T + 1])
    S2 = sum(W[T + 1:])
    abs_list.append(abs(S1 - S2))
    abs_min = min(abs_list)

print(abs_min)

