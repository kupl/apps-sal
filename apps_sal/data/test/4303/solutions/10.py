N, K = list(map(int, input().split()))
x = list(map(int, input().split()))


l = []
for i in range(N - K + 1):
    left = i
    right = i + K - 1
    ans1 = abs(x[left]) + abs(x[right] - x[left])
    ans2 = abs(x[right]) + abs(x[right] - x[left])
    tmp_ans = min(ans1, ans2)
    l.append(tmp_ans)

ans = min(l)
print(ans)
