N, K = list(map(int, input().split()))
x = list(map(int, input().split()))


l = []
# 連続するK本の選び方について、左端は0,1,2,...,N-K
for i in range(N - K + 1):
    left = i
    right = i + K - 1
    # leftが先、rightが後の場合
    ans1 = abs(x[left]) + abs(x[right] - x[left])
    # rightが先、leftが後の場合
    ans2 = abs(x[right]) + abs(x[right] - x[left])
    tmp_ans = min(ans1, ans2)
    l.append(tmp_ans)

ans = min(l)
print(ans)

