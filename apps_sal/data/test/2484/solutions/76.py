n = int(input())
aaa = list(map(int, input().split()))
right = 0
sum = 0
cnt = 0
for left in range(n):
    while right < n and sum ^ aaa[right] == sum + aaa[right]:
        sum += aaa[right]
        right += 1
    cnt += right - left
    if left == right:
        right += 1
    else:
        sum -= aaa[left]
print(cnt)
