N = int(input())
a_l = [int(a) for a in input().split()]
ans = 0
right = 0
_sum = 0
for left in range(N):
    while right < N and _sum ^ a_l[right] == _sum + a_l[right]:
        _sum += a_l[right]
        right += 1
    ans += right - left
    if right == left:
        right += 1
    else:
        _sum -= a_l[left]
print(ans)
