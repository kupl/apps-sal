
N = int(input())
W = list(map(int, input(). split()))


difference_list = []
for T in range(N - 1):
    S_left = sum(W[:T + 1])
    S_right = sum(W[T + 1:])

    difference_list.append(abs(S_left - S_right))  # 差のリストを作成

    ans = min(difference_list)

print(ans)
