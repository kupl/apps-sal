N = int(input())
A = list(map(int, input().split()))

# 左から順にやるとうまくいかない => [1, 4, 3, 2, 1] みたいな場で失敗
# 右から順に考えよ！
ans = 'Yes'
for i in range(N - 1, 0, -1):
    if A[i] < A[i - 1]:
        A[i - 1] -= 1
    if A[i] < A[i - 1]:
        ans = 'No'
        break

print(ans)
