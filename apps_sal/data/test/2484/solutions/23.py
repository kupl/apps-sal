N = int(input())
numbers = list(map(int, input().split()))
(summ, right, left) = (0, 0, 0)
ans = 0
for left in range(N):
    while right < N and summ + numbers[right] == summ ^ numbers[right]:
        summ += numbers[right]
        right += 1
    ans += right - left
    if right == left:
        right += 1
    else:
        summ -= numbers[left]
print(ans)
