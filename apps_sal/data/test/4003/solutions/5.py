n = int(input())
ai = list(map(int, input().split()))
ans = 0
ans2 = ''
num = 0
left = 0
right = n - 1
flag = 0
for i in range(n):
    if ai[left] <= num:
        if ai[right] <= num:
            break
        num = ai[right]
        ans += 1
        right -= 1
        ans2 += 'R'
        continue
    if ai[right] <= num:
        if ai[left] <= num:
            break
        num = ai[left]
        ans += 1
        left += 1
        ans2 += 'L'
        continue
    if ai[left] > ai[right]:
        num = ai[right]
        ans += 1
        right -= 1
        ans2 += 'R'
    elif ai[left] == ai[right]:
        if left == right:
            ans += 1
            ans2 += 'L'
            break
        flag = 1
        break
    else:
        num = ai[left]
        ans += 1
        left += 1
        ans2 += 'L'
if flag == 1:
    left2 = left
    temp = 0
    num2 = num
    while left2 < right:
        if ai[left2] > num2:
            temp += 1
            num2 = ai[left2]
        else:
            break
        left2 += 1
    temp2 = 0
    right2 = right
    num2 = num
    while right2 > left:
        if ai[right2] > num2:
            temp2 += 1
            num2 = ai[right2]
        else:
            break
        right2 -= 1
    if temp >= temp2:
        ans += temp
        ans2 += 'L' * temp
    else:
        ans += temp2
        ans2 += 'R' * temp2
print(ans)
print(ans2)
