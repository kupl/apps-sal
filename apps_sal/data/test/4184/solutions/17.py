N = int(input())
W = list(map(int, input(). split()))

difference_list = []
for T in range(N - 1):
    S_left = sum(W[:T + 1])  # Tまでの合計
    S_right = sum(W[T + 1:])  # Tより大きいグループの合計
    # print(W[:T+1],W[T+1:])  # WリストをTで分割
    difference_list.append(abs(S_left - S_right))
    ans = min(difference_list)

print(ans)
