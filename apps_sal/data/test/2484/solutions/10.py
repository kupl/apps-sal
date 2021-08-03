n = int(input())
a = list(map(int, input().split()))

right = 0
sum = 0
ans = 0

for left in range(n):
    while right < n and sum ^ a[right] == sum + a[right]:
        sum += a[right]
        right += 1
    ans += right - left
    if right == left:
        right += 1
    else:
        sum -= a[left]

print(ans)
