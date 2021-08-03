n = int(input())
s = list(input().rstrip())

left_cur = 0
right_cur = n - 1
ans = 0
flag = False
while(left_cur < right_cur and left_cur < n - 1 and right_cur > 0):
    while(s[left_cur] == 'R'):
        left_cur += 1
        if (left_cur == n - 1):
            flag = True
            break
    while(s[right_cur] == 'W'):
        right_cur -= 1
        if (right_cur == 0):
            flag = True
            break
    if(left_cur > right_cur):
        flag = True
    if(flag):
        break
    ans += 1
    left_cur += 1
    right_cur -= 1

print(ans)
