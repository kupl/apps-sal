n = int(input())
st = [0] * n
top = -1
curr_speed = 0
ans = 0
c = 0
while(n > 0):

    n -= 1
    a = list(map(int, input().split()))
    if(a[0] == 1):
        curr_speed = a[1]
        if(top >= 0 and curr_speed > st[top]):
            while(curr_speed > st[top] and top >= 0):
                top -= 1
                ans += 1

    if(a[0] == 4):
        c = 0
    elif(a[0] == 6):
        c += 1
    if(a[0] == 5):
        top = -1

    if(a[0] == 2):
        ans += c
        c = 0
    if(a[0] == 3):
        if(curr_speed > a[1]):
            ans += 1
        else:
            st[top + 1] = a[1]
            top += 1
print(ans)
